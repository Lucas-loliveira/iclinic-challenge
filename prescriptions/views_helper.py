class PrescriptionsViewHelper():


    def format_post_request(self, request_data):
        required_fields = ['id_physician', 'id_patient','text']
        result = {}

        result['id_physician'] = request_data.get("physician", {}).get('id', None)
        result['id_clinic'] = request_data.get("clinic", {}).get('id', None)
        result['id_patient'] = request_data.get("patient", {}).get('id', None)
        result['text'] = request_data.get("text", None)

        for required_field in required_fields:
            if not result[required_field]:
                return False

        return result

    def format_response(self, response_data):
        response = {
            "data": {
                "id": response_data.get("id", None),
                "clinic": {
                "id": response_data.get("id_clinic", None)
                },
                "physician": {
                "id": response_data.get("id_physician", None)
                },
                "patient": {
                "id": response_data.get("id_patient", None)
                },
                "text": response_data.get("text", None),
            }
        }

        return response