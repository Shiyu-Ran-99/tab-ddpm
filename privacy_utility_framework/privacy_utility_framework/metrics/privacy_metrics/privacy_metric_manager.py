from typing import Union, List, Dict

from privacy_utility_framework.privacy_utility_framework.metrics.privacy_metrics import PrivacyMetricCalculator


class PrivacyMetricManager:
    """
    A manager for handling multiple privacy metric calculators, enabling batch addition and evaluation of metrics.
    """
    def __init__(self):
        # Initialize an empty list to store instances of privacy metric calculators
        self.metric_instances = []

    def add_metric(self, metric_instance: Union[PrivacyMetricCalculator, List[PrivacyMetricCalculator]]):
        """
        Adds one or multiple metric instances to the manager.

        Parameters
        ----------
        metric_instance : Union[PrivacyMetricCalculator, List[PrivacyMetricCalculator]]
            A single metric instance or a list of metric instances to add to the manager.
        """
        # Check if the input is a list of instances or a single instance and handle accordingly
        if isinstance(metric_instance, list):
            for metric in metric_instance:
                self._add_single_metric(metric)
        else:
            self._add_single_metric(metric_instance)

    def _add_single_metric(self, metric_instance: PrivacyMetricCalculator):
        """
        Adds a single metric instance to the manager.

        Parameters
        ----------
        metric_instance : PrivacyMetricCalculator
            An instance of a privacy metric to add.

        Raises
        ------
        TypeError
            If `metric_instance` is not a subclass of `PrivacyMetricCalculator`.
        """
        # Ensure the provided metric is a valid subclass of PrivacyMetricCalculator
        if not isinstance(metric_instance, PrivacyMetricCalculator):
            raise TypeError("Metric class must be a subclass of PrivacyMetricCalculator.")

        try:
            # Append the metric instance to the list of managed metrics
            self.metric_instances.append(metric_instance)
        except Exception as e:
            print(f"Error creating metric instance: {e}")

    def evaluate_all(self) -> Dict[str, float]:
        """
        Evaluates all added metrics and returns their results.

        Returns
        -------
        Dict[str, float]
            A dictionary where keys are metric names concatenated with the dataset names and values are the evaluated metric scores.
        """
        results = {}
        for metric in self.metric_instances:
            # Retrieve the class name of each metric instance as its identifier
            metric_name = metric.__class__.__name__
            datasets_names = f"{metric.original.name, metric.synthetic.name}"
            # Evaluate the metric and store the result in the dictionary
            results[metric_name+datasets_names] = metric.evaluate()
        return results