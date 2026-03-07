from kissut import LoggingTestCase
from efficient_args.parseArgs import parseCmdLineList

TEST_FILE = "tests/itemList.txt"
TEST_FILE_WITH_BLANKS = "tests/itemListBlanks.txt"


class TestParsing(LoggingTestCase):
    def test_a_list(self):
        cmds = {"list": ["a", "b", "c"]}
        lst = parseCmdLineList(cmds)
        self.assertTrue("a" in lst)

    def test_b_file(self):
        cmds = {"list": [], "file": TEST_FILE}
        lst = parseCmdLineList(cmds)
        self.logger.debug("List: {}".format(lst))
        self.assertTrue("x44" in lst)
        self.assertEqual(3, len(lst))

    def test_c_file(self):
        cmds = {"list": [], "file": TEST_FILE_WITH_BLANKS}
        lst = parseCmdLineList(cmds)
        self.logger.debug("List: {}".format(lst))
        self.assertTrue("x55" in lst)
        self.assertEqual(4, len(lst))
