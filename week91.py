try:
    n=int(input())
    raise Exception
except(TypeError):
    print("Type error")
except ValueError:
    print("Value error")
except KeyboardInterrupt:
    print("Keyboard interrupt")
finally:
    print("final block")