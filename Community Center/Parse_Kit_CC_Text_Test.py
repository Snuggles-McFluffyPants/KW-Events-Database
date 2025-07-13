import unittest
from Parse_Kit_CC_Text import parse_text

Good_list1 = [
    ["Knitting (In stitches)", "#160347/55 yrs +/Openings 0", "Breithaupt Centre", "September 5, 2024 to August 28, 2025", "Thu 1:00 PM - 3:00 PM", "Free", "In progress"],
    ["Euchre", "#160345/18 yrs +/Openings 23", "Breithaupt Centre", "September 6, 2024 to August 29, 2025", "Fri 12:45 PM - 3:45 PM", "Free", "Enroll Now", "In progress"],
    ["Fun in the Sun", "#185468/Age at least 4 yrs but less than 7 yrs/Openings 0", "Stanley Park Community Centre - Outdoors", "August 8, 2025", "Fri 1:00 PM - 2:00 PM", "View fee details"]]
test_string1 = "Skip to main content\nEnglish\nSign In |Create an Account\nHome\nRegister for Activities\nFacilities\nActivity Calendars\nMemberships\nMy Cart\nhome>\nactivity search\nActivity search\nSearch by keyword OR by number\nSearch\nWhen\nWhere\nWho\nActivities\nOpen spots\nIn progress / Future\nFound 2064 matching result(s)\nSort by:\nDate range\nMap view\nFull\nKnitting (In stitches)\n#160347/55 yrs +/Openings 0\nBreithaupt Centre\nSeptember 5, 2024 to August 28, 2025\nThu 1:00 PM - 3:00 PM\nFree\nIn progress\nEuchre\n#160345/18 yrs +/Openings 23\nBreithaupt Centre\nSeptember 6, 2024 to August 29, 2025\nFri 12:45 PM - 3:45 PM\nFree\nEnroll Now\nIn progress\nFun in the Sun\n#185468/Age at least 4 yrs but less than 7 yrs/Openings 0\nStanley Park Community Centre - Outdoors\nAugust 8, 2025\nFri 1:00 PM - 2:00 PM\nView fee details\nCity of Kitchener\n200 King St. W.\nKitchener, ON N2G 4G7\nTel. (519) 741.2907\nEmail: activenet@kitchener.ca\nMethods of Payment\nVisa, MasterCard, Other\nHave Questions?\nOnline Registration FAQs\nConnect with Kitchener\nTerms of Use\nCopyright Policy\nPrivacy Notice\nCity of Kitchener's Policies: Terms of Use\nYour Privacy Rights\n© 2025 Active Network, LLC and/or its affiliates and licensors. All rights reserved."

class MyTestCase(unittest.TestCase):
    def test_parse_text_test_string1(self):
        print(parse_text(test_string1))
        self.assertEqual(parse_text(test_string1), Good_list1)


if __name__ == '__main__':
    unittest.main()
