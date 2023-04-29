# Import required modules
from thompson_sampling.bernoulli import BernoulliExperiment
from thompson_sampling.priors import BetaPrior
from pandas import Series

# Define the ThompsonSampling class
class ThompsonSampling():
  def __init__(self, labels):
    """
      Initializes the Thompson Sampling object.
      Args:
          labels (list): A list of labels for each arm.
    """
    # Initialize the means, variances, and effective sizes of the arms
    self.means = [0.5 for i in range(len(labels))]  # The initial mean value of each arm is 0.5
    self.variances = [0.1 for i in range(len(labels))]  # The initial variance of each arm is 0.1
    self.effective_sizes = [10 for i in range(len(labels))]  # The initial effective size of each arm is 10
    self.labels = labels  # A list of labels for each arm

    # Create a BetaPrior object to store the prior information for each arm
    pr = BetaPrior()
    pr.add_multiple(Series(self.means), 
                    Series(self.variances), 
                    Series(self.effective_sizes), 
                    Series(self.labels)
                )
    
    # Create a BernoulliExperiment object to run the Thompson sampling algorithm
    self.experiment = BernoulliExperiment(priors = pr)

  def draw_arm(self):
    """
      Chooses an arm to pull using Thompson Sampling.
      Returns:
              The chosen arm.
    """
    # Choose an arm using the Thompson sampling algorithm
    arms = self.experiment.choose_arm()
    return arms
  
  def update_arm(self, Result, operator):
    """
      Updates the parameters of the chosen arm based on the result of the operator's action.
      Args:
          Result (bool): A boolean indicating whether the operator succeeded or failed.
          operator (str): The label of the arm that was chosen by the operator.
    """
    try:
      rewards = []
      if Result:
        # If the result is positive, give a reward of 1 to the selected arm and 0 to the other arms
        for i in self.labels:
          if str(i) == str(operator):
            rewards.append({"label":i, "reward":1})
          else:
            rewards.append({"label":i, "reward":0})
      else:
        # If the result is negative, give a reward of -1 to the selected arm and 0 to the other arms
        for i in self.labels:
          if str(i) == str(operator):
            rewards.append({"label":i, "reward":-1})
          else:
            rewards.append({"label":i, "reward":0})

      # Update the priors of the arms using the rewards
      self.experiment.add_rewards(rewards)
    except Exception as e:
      # Print an error message if an exception is raised
      print(f"Thompson Sampling Class Error: {e}\n") 
