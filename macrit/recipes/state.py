from abc import ABC, abstractmethod

# Common state class for all states to be called
class State(ABC):
	@property
	def user(self) -> User:
		return self._user

	@user.setter
	def user(self, user: User) -> None:
		self._user = user


	@abstractmethod
	def subscribe(self) -> None:
		pass
	
	@abstractmethod
	def unsubscribe(self) -> None:
		pass

	
class Subscribe(State):
    # if up button is pushed, move upwards then it changes its state to second floor.
    def unsubscribe(self) -> None:
        print("You have unsubscribed")
        self.user.setUser(Unsubscribe())

    # 
    def subscribe(self) -> None:
        print("You are already subscribed")


class Unsubscribe(State):
    # if up button is pushed, move upwards then it changes its state to second floor.
    def subscribe(self) -> None:
        print("You have subscribed")
        self.user.setUser(Subscribe())

    def unsubscribe(self) -> None:
        print("You have already unsubscribed")
        #output error message