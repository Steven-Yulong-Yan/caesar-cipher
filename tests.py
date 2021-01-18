#!/usr/bin/env python3
from test_util import OrderedTestCase, TestMaster
from test_util import RedirectStdIO, skipIfFailed

# pylint: disable=E1101
import caesar_cipher


class TestDesign(OrderedTestCase):
    def test_encrypt_defined(self):
        self.assertFunctionDefined(caesar_cipher, 'encrypt', 2)

    def test_decrypt_defined(self):
        self.assertFunctionDefined(caesar_cipher, 'decrypt', 2)

    def test_find_encryption_offsets_defined(self):
        self.assertFunctionDefined(caesar_cipher, 'find_encryption_offsets', 1)

    def test_main_defined(self):
        self.assertFunctionDefined(caesar_cipher, 'main', 0)

    @skipIfFailed(test_name='test_encrypt_defined')
    @skipIfFailed(test_name='test_decrypt_defined')
    @skipIfFailed(test_name='test_find_encryption_offsets_defined')
    @skipIfFailed(test_name='test_main_defined')
    def test_docs(self):
        self.assertDocString(caesar_cipher.encrypt)
        self.assertDocString(caesar_cipher.decrypt)
        self.assertDocString(caesar_cipher.find_encryption_offsets)
        self.assertDocString(caesar_cipher.main)


class TestFunctions(OrderedTestCase):
    @skipIfFailed(TestDesign, 'test_encrypt_defined')
    def test_encrypt(self):
        self.assertEqual(caesar_cipher.encrypt("you will always remember this as the day", 7),
                         'fvb dpss hsdhfz yltltily aopz hz aol khf')
        self.assertEqual(caesar_cipher.encrypt("music is the shorthand of emotion", 2),
                         'owuke ku vjg ujqtvjcpf qh goqvkqp')
        self.assertEqual(caesar_cipher.encrypt("qgnrag hgorkey gtj cnovvkj ixkgs", 9),
                         'zpwajp qpxatnh pcs lwxeets rgtpb')

    @skipIfFailed(TestDesign, 'test_decrypt_defined')
    def test_decrypt(self):
        self.assertEqual(caesar_cipher.decrypt("a bmkl kso lzw sv sfv lzgmyzl al dggcwv xmf", 17),
                         'j kvtu tbx uif be boe uipvhiu ju mpplfe gvo')
        self.assertEqual(caesar_cipher.decrypt("a bmkl kso lzw sv sfv lzgmyzl al dggcwv xmf", 18),
                         'i just saw the ad and thought it looked fun')
        self.assertEqual(caesar_cipher.decrypt("asdf ghjkl qwerty uiop z xcvbnm", 17),
                         'jbmo pqstu zfnach drxy i glekwv')

    @skipIfFailed(TestDesign, 'test_find_encryption_offsets_defined')
    def test_find_encryption_offsets(self):
        self.assertEqual(caesar_cipher.find_encryption_offsets(
            "iynjo fuhsudj ev jxu jycu yj mehai qbb jxu jycu"), (16,))
        self.assertEqual(caesar_cipher.find_encryption_offsets(
            "vftg amnl aqkkxmn mjmcqlm emkveoxtmn lvbmlomz"), ())
        self.assertEqual(caesar_cipher.find_encryption_offsets("nmd"), (4, 12, 21, 25))


class TestMain(OrderedTestCase):
    @skipIfFailed(TestDesign, 'test_main_defined')
    def test_example_main(self):
        with open('data_files/example_inputs.txt') as fin, \
                open('data_files/example_output.txt') as fout:
            inputs = fin.read()
            outputs = fout.read()

        with RedirectStdIO(stdin=True, stdout=True) as stdio:
            stdio.set_stdin(inputs)
            caesar_cipher.main()

        self.assertMultiLineEqual(stdio.stdout, outputs)


class TestExtension(OrderedTestCase):
    @skipIfFailed(TestDesign, 'test_main_defined')
    def test_extension_encrypt(self):
        with open('data_files/example_extension_inputs.txt') as fin, \
                open('data_files/example_extension_output.txt') as fout:
            inputs = fin.read()
            outputs = fout.read()

        with RedirectStdIO(stdin=True, stdout=True) as stdio:
            stdio.set_stdin(inputs)
            caesar_cipher.main()

        self.assertMultiLineEqual(stdio.stdout, outputs)

    @skipIfFailed(TestDesign, 'test_main_defined')
    def test_extension_autodecrypt(self):
        with open('data_files/example_extension_inputs_2.txt') as fin, \
                open('data_files/example_extension_output_2.txt') as fout:
            inputs = fin.read()
            outputs = fout.read()

        with RedirectStdIO(stdin=True, stdout=True) as stdio:
            stdio.set_stdin(inputs)
            caesar_cipher.main()

        self.assertMultiLineEqual(stdio.stdout, outputs)


def main():
    test_cases = [
        TestDesign,
        TestFunctions,
        TestMain,
        TestExtension,
    ]

    master = TestMaster(max_diff=None)
    master.run(test_cases)


if __name__ == '__main__':
    main()
