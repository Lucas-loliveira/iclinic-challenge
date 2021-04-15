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

