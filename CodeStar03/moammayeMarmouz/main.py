import re


def clean_text(text: str):
    text = text.lower()
    text = re.sub('[\W_]+', ' ', text)
    text = re.sub(' +', ' ', text).strip()

    stopwords = ["a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no",
                 "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this",
                 "to", "was", "will", "with"]
    cleaned_text = ' '.join([txt for txt in text.split(" ") if txt not in stopwords])
    return cleaned_text


def create_vocabulary(docs):
    vocabs = set(word for doc in docs for word in doc.split(" "))
    return list(vocabs)


def create_inverted_index(docs, vocabulary):
    inverted_index = dict()
    for vocab in vocabulary:
        inverted_index[vocab] = [idx + 1 for idx, doc in enumerate(docs) if (' ' + vocab + ' ') in (' ' + doc + ' ')]

    return inverted_index


def parse_queries(queries):
    def set_nested_value(d, keys, value):
        for key in keys[:-1]:
            if key not in d:
                d[key] = {}
            d = d[key]
        d[keys[-1]] = value

    result = []

    for query in queries:
        temp_dict = {}
        # Split by commas to handle multiple key-value pairs on the same line
        pairs = query.split(',')

        for pair in pairs:
            if '=' in pair:
                key, value = pair.split('=', 1)

                # Split the key by '.' to handle nested keys
                keys = []
                while '[' in key:
                    base, rest = key.split('[', 1)
                    index, rest = rest.split(']', 1)
                    keys.append(base)
                    keys.append(int(index))
                    key = rest.strip('.')

                if key:
                    keys.append(key)

                # Set the value in the nested dictionary structure
                set_nested_value(temp_dict, keys, value)

        result.append(temp_dict)

    return result


def main():
    def documentRecovery(term):
        result = inverted_index[term] if term in inverted_index else set()
        return list(result)

    def match(term):
        result = [idx + 1 for idx, doc in enumerate(docs) if term in doc]
        return result if result else set()

    def matchQuery(term):
        return match(term) if len(term.split(" ")) > 1 else documentRecovery(term)

    def allQuery(results):
        results = [r if isinstance(r, set) else set(r) for r in results]
        return set.intersection(*results)

    def anyQuery(results):
        results = [r if isinstance(r, set) else set(r) for r in results]
        return set.union(*results)

    def orQuery(results):
        results = [r if isinstance(r, set) else set(r) for r in results]
        return set.union(*results)

    def andQuery(results):
        results = [r if isinstance(r, set) else set(r) for r in results]
        return set.intersection(*results)

    def notQuery(result, exclude):
        if not isinstance(result, set):
            result = set(result)
        if not isinstance(exclude, set):
            exclude = set(exclude)
        return result.difference(exclude)

    def sizeQuery(result_set, n):
        if not isinstance(result_set, set):
            result_set = set(result_set)
        return set(list(result_set)[:n])

    def execute_nested_query(query):
        if isinstance(query, dict):
            combined_result = set()

            for key, value in query.items():
                if key == 'match':
                    combined_result = matchQuery(value)
                elif key == 'all':
                    results = [execute_nested_query(v) if isinstance(v, dict) else matchQuery(v) for v in
                               value.values()]
                    combined_result = allQuery(results)
                elif key == 'any':
                    results = [execute_nested_query(v) if isinstance(v, dict) else matchQuery(v) for v in
                               value.values()]
                    combined_result = anyQuery(results)
                elif key == 'or':
                    results = [execute_nested_query(v) if isinstance(v, dict) else matchQuery(v) for v in
                               value.values()]
                    combined_result = orQuery(results)
                elif key == 'and':
                    results = [execute_nested_query(v) if isinstance(v, dict) else matchQuery(v) for v in
                               value.values()]
                    combined_result = andQuery(results)
                elif 'not' in key:
                    base_result = set(range(1, num_docs + 1))
                    exclude_result = execute_nested_query({key.split('.')[1]: value})
                    combined_result = notQuery(base_result, exclude_result)
                elif key == 'size':
                    combined_result = sizeQuery(combined_result, int(value))
                else:
                    # For other non-function keys or nested structures
                    nested_result = execute_nested_query(value)
                    if not combined_result:
                        combined_result = nested_result
                    else:
                        combined_result = combined_result.intersection(nested_result)

            return combined_result

        return set()

    ## Documents
    num_docs = int(input())
    docs = [clean_text(input()) for _ in range(num_docs)]
    print(docs)
    vocabs = create_vocabulary(docs)
    inverted_index = create_inverted_index(docs, vocabs)

    ## Queries
    num_queries = int(input())
    queries = [input() for _ in range(num_queries)]
    parsed_queries = parse_queries(queries)
    for query in parsed_queries:
        result_list = sorted(execute_nested_query(query))
        result_string = ' '.join(map(str, result_list)) if result_list else "NO RESULT"
        print(result_string)


if __name__ == "__main__":
    main()
