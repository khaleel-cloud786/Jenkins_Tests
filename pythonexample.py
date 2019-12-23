class Message():
    def printMessage(self):
        """
        a simple function that prints a message
        """

    from termcolor import colored
    print(colored('YAHOO IT WORKS.........!', 'red'), colored('Lets Work on the Second example', 'green'))

if __name__ == "__main__":
    msg = Message()
    msg.printMessage()
