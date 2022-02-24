from src.simple_python import SimplePython
import sys

def main(user_input):
    app = SimplePython()
    app.run()

if __name__ == "__main__":
    main(sys.argv[1:])
