

class CustomActionsAPI(Resource):

    def get(self):

        # check if result can be served from cache
        if r.exists("all_custom_actions"):
            return json.loads(r.get("all_custom_actions"))
        else:
            # Get results and update the cache with new values
            logging.debug('getting Data from DB')
            result = CustomActionsModel.get_all_custom_actions()
            r.set("all_custom_actions", json.dumps(result), ex=GLOBAL_EXPIRY)
            return result

    def post(self):
        json_data = request.get_json(force=True)
        result = CustomActionsModel.create_action(json_data)

        # Clear redis cache
        r.delete("all_custom_actions")
        return result

    def put(self):

        # Updating record
        json_data = request.get_json(force=True)
        result = CustomActionsModel.update_action(json_data)

        # Clear redis cache
        r.delete("all_custom_actions")
        return result

    def delete(self):
        # Deleting record
        json_data = request.get_json()
        result = CustomActionsModel.delete_action(json_data)

        # Clear redis cache
        r.delete("all_custom_actions")
        return result



class Conversations(Resource):
    def get(self, conversation_id):

        result = ConversationsModel.get_conversations(conversation_id)
        return result
