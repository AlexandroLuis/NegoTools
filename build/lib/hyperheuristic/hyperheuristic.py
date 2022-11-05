from thompson_sampling.bernoulli import BernoulliExperiment
from thompson_sampling.priors import BetaPrior

from pandas import Series

class ThompsonSampling():
  def __init__(self, labels):
    self.means = Series([0.5, 0.5, 0.5, 0.5])
    self.variances = Series([0.1, 0.1, 0.1, 0.1])
    self.effective_sizes = Series([10, 10, 10, 10])
    self.labels = labels

    pr = BetaPrior()
    pr.add_multiple(self.means, self.variances, self.effective_sizes, Series(self.labels))
    
    self.experiment = BernoulliExperiment(priors = pr)

  def draw_arm(self):
    arms = self.experiment.choose_arm()
    return arms
  
  def update_arm(self, Result, operator):
    try:
      rewards = []
      if Result:
        for i in self.labels:
          if str(i) == str(operator):
            rewards.append({"label":i, "reward":1})
          else:
            rewards.append({"label":i, "reward":0})
      else:
        for i in self.labels:
          if str(i) == str(operator):
            rewards.append({"label":i, "reward":-1})
          else:
            rewards.append({"label":i, "reward":0})

      self.experiment.add_rewards(rewards)
    except Exception as e:
      print(f"Thompson Sampling Class Error: {e}\n") 

