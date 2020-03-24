"""
Contains Business logic
"""

from src.services.manager.entity_manager import IEntityManager


class QuizManager(IEntityManager):
    """
    Manage quiz entities
    """
    def fetchall(self) -> int:
        """
        Return the number of rows
        """
        return self.data_store.read(self.name)

    def add_record(self, request_data) -> None:
        """
        Add quiz
        """
        
        my_list = self.get_attribute_list(request_data)

        for my_dict_data in my_list:
            self.data_store.write([self.name, 'category', 'question', 'options_1', 'options_2',
                                   'option_3', 'option_4', 'answer'],
                                  [my_dict_data['category'], my_dict_data['question'],
                                   my_dict_data['options_1'], my_dict_data['options_2'],
                                   my_dict_data['options_3'], my_dict_data['options_4'],
                                   my_dict_data['answer']])

    def get_attribute_list(self, request_data) -> list:
        """
        get attribute list
        """
        
        question_list = []
        for val in request_data.values():
            for key_item, val_item in val.items():
                self.get_attribute_dict(val_item, key_item, question_list)

        return question_list

    def get_attribute_dict(self, category_item_wise, category, question_list) -> list:
        """
        Get Attribute list
        """

        for val in category_item_wise.values():

            record = {'category': category, 'question': val['question'],
                      'options_1': val['options'][0], 'options_2': val['options'][1],
                      'options_3': val['options'][2], 'options_4': val['options'][3],
                      'answer': val['answer']}

            question_list.append(record)
