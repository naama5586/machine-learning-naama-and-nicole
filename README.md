# Clustering Driver Types In A Car Simulator

## Summary

The purpose of the project is to try to identify types of drivers in a driving simulator by studying and comparing the performance of different clustering algorithms in combination with various feature selection techniques for unsupervised learning tasks. We aim to assess the effectiveness of DBSCAN, KMeans, and Agglomerative Clustering algorithms along with feature selection methods such as PCA, Kernel PCA, and ICA in identifying significant patterns in the data. The evaluation includes cluster quality assessment using silhouette scores, the Davies-Bouldin index, and the Calinski-Harabasz index, providing insight into the appropriateness of different combinations of feature selection algorithms and methods.

We aim to determine if there are drivers less suitable to be remote drivers in the autonomous vehicle world. Among the models tested, KMeans with ICA feature selection yielded particularly promising results, demonstrating the best evaluation metrics. Relative to the size of the data, this model effectively segmented it into groups of drivers, revealing distinct trends within each group. We believe this project holds significance, especially for the research team, as more information is collected in the simulator. With additional data, we anticipate that the model's results will become even more accurate.

## Installation

To install and run this project, follow these steps:

1. Download the necessary data files from the repository:
   - [Spatial_after_droping_missing_values3.csv](link_to_csv_file)
   - [participation_data.csv](link_to_csv_file)

2. Ensure you have the required libraries installed. You can install them using pip:

```bash
pip install pandas numpy matplotlib scikit-learn
```

3. Once the data files are downloaded and the libraries are installed, you can run the provided code to read the files:

```python
import pandas as pd

# Read the data files
data = pd.read_csv("path/to/Spatial_after_droping_missing_values3.csv")
data2 = pd.read_csv("path/to/participation_data.csv")
```

4. You can then proceed to execute the remaining code provided in the repository.

## Credits

We would like to acknowledge Professor Oren Musiknet for providing the data from his laboratory and for his valuable guidance and support throughout the project.

## Contact

For any questions, feedback, or inquiries, feel free to contact us:

- Naama Bouskila: [naama5586@gmail.com](mailto:naama5586@gmail.com)
- Nicole Ben Haim: [nicolaybh29@gmail.com](mailto:nicolaybh29@gmail.com)
