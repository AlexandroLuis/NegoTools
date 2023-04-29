# 🚀 Welcome to NegoTools 🚀

NegoTools is an easy-to-use Python library that combines scientific, statistical, machine learning, time series, forecasting, hyper heuristics, deep learning, stats tests, and more. It provides a powerful and intuitive interface that's perfect for researchers, engineers, and anyone who needs to analyze data quickly and accurately.

## 💪 Features

With NegoTools, you can:

- 🤖 Perform regression and classification tasks using state-of-the-art machine learning algorithms
- 📊 Explore your data using powerful statistical analysis tools
- 🎲 Run multi-armed bandit experiments to optimize your decision-making
- ⏰ Conduct time series analysis and forecasting to make predictions about the future
- 🧠 Use hyper-heuristic techniques to optimize complex systems
- 🌟 Implement deep learning models for advanced data analysis
- 📈 Perform a wide range of statistical tests to make confident decisions about your data

## 🎉 Getting started

To get started with NegoTools, simply install it using `pip`:

```shell
pip install negotools
```

Then, import the library and start using its features in your Python code, here an example of Hyper Heuristics usage:

```python
# import thompson sampling from hyperheuristic
from hyperheuristic import ThompsonSampling as TS

# create a thompson sampling object from a list of arms
ts = TS(["Cat", "Dog", "Bee", "Panda", "Bear"])

# draw an arm
arm = ts.draw_arm()
print(arm)

# update arm if it's better or worse than the last selected
# input a bool - True or False and then the arm
ts.update_arm(False, arm)
```

## 🤝 Contributing

We welcome contributions from anyone who's interested in improving NegoTools. To contribute, simply fork this repository, make your changes, and submit a pull request. We'll review your changes and merge them if they meet our guidelines.

## 📝 License

NegoTools is released under the MIT License. See `LICENSE` for more information.

## 📞 Contact

If you have any questions or feedback about NegoTools, please don't hesitate to contact us. You can reach us by email at [negotools@kawahib.com](mailto:negotools@kawahib.com).