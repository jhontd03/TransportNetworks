from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import pandas as pd
import scipy.cluster.hierarchy as sch

def cluster_graph(X_data: pd.Series, labels: pd.Series, 
                  title_graph: str, map_color: str='tab20'):
    """
    Genera gráfico de dispersión del set de datos con las etiquetas
    de cada cluster 
    :param X_data: pd.Series
            Datos con las variables de estudio.
    :param labels: pd.Series
             Etiquetas obtenidas por el método de clúster.            
    :param title_graph: str
            Título del gráfico.
    :param map_color: str
            mapa de color
            default: 'tab20'
    :return: None
    """
    plt.title(title_graph)
    plt.scatter(X_data.iloc[:,0], X_data.iloc[:,1], s=15, c=labels, alpha=.5, cmap=map_color)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()


def eps_graph(X_data: pd.Series, minpts: int) -> None:   
    """
    Genera gráfico para determinar el número optimo de eps
    :param X_data: pd.Series
            Serie con las variables de estudio.
    :param minpts: int
            Mínimo número de puntos dentro de la región de épsilon.
    :return: None
    """
    neigh = NearestNeighbors(n_neighbors=minpts)
    nbrs = NearestNeighbors(n_neighbors=minpts, algorithm='ball_tree').fit(X_data) 
    distances, _ = nbrs.kneighbors(X_data)
    k_dist = [x[-1] for x in distances]
    plt.figure()
    plt.style.use("seaborn-notebook")
    plt.plot(sorted(k_dist))
    plt.xlabel('k-distance')
    plt.ylabel('eps')
    plt.grid()
    plt.show()

def cluster_hierarchy(X_data: pd.Series) -> None:
    """
    Genera dendograma para cada criterio de enlace
    :param X_data: pd.Series
            Series de datos con las variables de estudio.
    :return: None
    """
    method_linkage = ['single', 'complete', 'centroid', 'median', 'average', 'ward']
    plt.figure(6, figsize=(16, 8))
    plt.clf()
    for k, v in enumerate(method_linkage):
        plt.subplot(2, 3, k+1)
        _ = sch.dendrogram(sch.linkage(X_data, method = v))
        plt.gca().axes.get_xaxis().set_visible(False)
        plt.title(v)
    plt.show()

def info_cluster(data: pd.DataFrame) -> list:
    """
    Crea lista con información asociada a cluster:
    area, número de puntos y el rattio area/# puntos, para cada cluster
    :param data: pd.DataFrame
            Dataframe con las variables de estudio.
    :return: list
                Contiene el area, número de puntos y el rattio area/# puntos
                para cada cluster 
    """
    lat_dist = data['Lat'].max() - data['Lat'].min()
    lon_dist = abs(data['Lon'].max() - data['Lon'].min())

    area_cluster = lat_dist*lon_dist
    num_points = len(data['Lat'])
    rt_point_area = num_points/area_cluster

    return [area_cluster, num_points, rt_point_area]