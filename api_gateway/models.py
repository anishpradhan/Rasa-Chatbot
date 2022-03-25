class CustomActionsModel:
    def __init__(self):
        pass

    def get_all_custom_actions(self):
        cursor = db.actions.find()
        return json.loads(dumps(list(cursor)))

    def create_action(self, record):

        json_record = json.loads(json.dumps(record))

        # Validation to check if action already exists

        val_res = db.actions.find_one({"action_name": json_record['action_name']})

        if val_res is not None:
            print('Action already exists')
            return {"status": "Error", "message": "Action already exists"}
        else:
            result = db.actions.insert_one(json_record)
            print("Action created {}".format(result.inserted_id))
            return {"status": "Success", "message": "Action Has Been Created"}

    def update_action(self, record):

        json_record = json.loads(json.dumps(record))

        query = {"_id": ObjectId("{}".format(json_record['object_id']))}
        update_field = {"$set": {"action_description": json_record['action_description']
                                 }}
        result = db.actions.update_one(query, update_field)
        print("Action Updated , rows modified {}".format(result))
        return {"status": "Success", "message": "Action details updated successfully "}

    def delete_action(self, record):

        json_record = json.loads(json.dumps(record))
        object_id = json_record['object_id']
        query = {"_id": ObjectId("{}".format(object_id))}

        # Delete Action
        result = db.actions.delete_one(query)
        print("Action Deleted count {}".format(result))
        return {"status": "Success", "message": "Action Deleted Successfully"}


class ConversationsModel:

    def __init__(self):
        pass

    def get_all_conversations(self, page_num, page_size):
        skips = int(page_size) * (int(page_num) - 1)
        cursor = db.conversations.find().sort('latest_event_time', -1).skip(skips).limit(int(page_size))
        return json.loads(dumps(list(cursor)))

    def get_conversations(self, sender_id):
        print("Pulling tracker data for a conversation")

        result = db.conversations.find_one({"sender_id": sender_id})
        return json.loads(dumps(result))
