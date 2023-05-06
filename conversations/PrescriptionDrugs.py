from conversations.BaseConversation import BaseConversation


class PrescriptionDrugRecommendations(BaseConversation):

    title = 'PrescriptionDrugs'
    opening_conversation = [
        {
            'role': 'user',
            'content': 'create a list of the top 20 prescription drugs'
        },
        {
            'role': 'user',
            'content': 'Provide brand name of the drug with one answer per line, no leading numbers or symbols, and no other commentary'
        }
    ]

    recommendations_conversation = [
        {
            'role': 'user',
            'content': 'I\'m taking the drug {name}'
        },
        {
            'role': 'user',
            'content': 'create a list of 10 other prescription drugs I am most likely to be taking'
        },
        {
            'role': 'user',
            'content': 'Provide brand name of the drug, one answer per line, no leading numbers or symbols, and no other commentary'
        }
    ]

    def clean_line(self, line):
        line = super(PerscriptionDrugRecommendations, self).clean_line(line)

        # clean up inconsistencies
        # TODO:

        return line
