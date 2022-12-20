import unittest
import emailotp
import re

class TestOtp(unittest.TestCase):

    def test_validmail1(self):
        email = 'sheetalwanghare123@gmail.com'
        emailotp.validate_email(email)
        otp = emailotp.generate_otp(5)
        emailotp.otp_length(otp)
        emailotp.send_otp(email,otp)

    def test_invalidmail(self):
        email = 'sheetalwanghare@iei@ail.com'
        emailotp.validate_email(email)
        otp = emailotp.generate_otp(5)
        emailotp.otp_length(otp)
        emailotp.send_otp(email, otp)

    def test_otplength(self):
        email = 'sheetalwanghare123@gmail.com'
        emailotp.validate_email(email)
        otp = emailotp.generate_otp(5)
        emailotp.otp_length(otp)
        emailotp.send_otp(email,otp)

    def test_otplength1(self):
        email = 'sheetalwanghare123@gmail.com'
        emailotp.validate_email(email)
        otp = emailotp.generate_otp(8)
        emailotp.otp_length(otp)
        emailotp.send_otp(email,otp)

if __name__ == '__main__':
    unittest.main()


