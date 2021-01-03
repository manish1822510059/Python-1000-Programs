def outerfact():
    print("hello i am a outer function")

    def innerfact():

        print("hello i am a inner function")

    innerfact()

outerfact()