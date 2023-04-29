# 🎲 Thompson Sampling API 🎲

This is a Python implementation of the Thompson Sampling algorithm, which is used for multi-armed bandit problems. The ThompsonSampling class can be used as an API to implement the algorithm in your own projects.

## 🚀 Getting Started

### 🔧 Installation

To install the package, you can use pip:
```shell
    pip install NegoTools
```
### 🛠️ Usage

To use the Thompson Sampling algorithm in your code, you need to import the required modules:
```python
    from hyperheuristic import ThompsonSampling as TS

Then, define the labels for each arm and initialize a ThompsonSampling object:

    labels = ["Arm 1", "Arm 2", "Arm 3"]
    ts = TS(labels)

To choose an arm using the Thompson Sampling algorithm, use the draw_arm() method:

    chosen_arm = ts.draw_arm()

To update the parameters of the chosen arm based on the result of the operator's action, use the update_arm() method:

    ts.update_arm(result, operator)
```
### 📝 Example

Here's an example of how to use the ThompsonSampling class:
```python
    # Import required modules
     from hyperheuristic import ThompsonSampling as TS

    # Define the labels for each arm
    labels = ["Arm 1", "Arm 2", "Arm 3"]

    # Initialize the ThompsonSampling object
    ts = TS(labels)

    # Choose an arm using the Thompson Sampling algorithm
    chosen_arm = ts.draw_arm()

    # Assume the operator succeeded and update the arm's parameters
    ts.update_arm(True, chosen_arm)
```
### 🤝 Contributing

Contributions are always welcome! If you want to contribute to the project, please follow these steps:

1. Fork the repository
2. Clone the repository to your local machine
3. Create a new branch
4. Make your changes and commit them
5. Push your changes to your fork
6. Create a pull request

### 📄 License

This project is licensed under the MIT License - see the LICENSE.md file for details.