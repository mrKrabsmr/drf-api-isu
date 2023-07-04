from elasticsearch_dsl import Q

class StandardSearch:

    def filter_queryset(self, request, view):
        params = request.query_params
        if not params:
            return view.service_class.get_update_queryset(view)
        text = params.get("text")
        if text:
            query = Q(
                name_or_query="match",
                query=text,
                fuzziness="AUTO",
            )
            result = view.document_class.search().query(query)
            view.queryset = result.to_queryset()
            del params["text"]
        return view.service_class.get_update_queryset(view, params)

