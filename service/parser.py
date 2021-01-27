from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('login', type=str, help='Login must be str')
parser.add_argument('password', type=str, help='Password must be str')
parser.add_argument('name', type=str, help='Name must be str')
parser.add_argument('last name', type=str, help='Last name must be str')
parser.add_argument('email', type=str, help='Email must be str')
parser.add_argument('sum', type=int, help='Sum must be int')
parser.add_argument('category', type=str, help='Category must be str')
parser.add_argument('type', type=str, help='Type must be str')

