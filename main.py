from process_raw_data import *

from cure_modified import cure
from pyclustering.utils import read_sample

def main():
    """
        main script that runs the cure algorithm.
    """
    # data preprocessing...
    path = './raw_data/Falen.txt'
    widths=[29,4,7,8,7,11,9,6]
    columns = ['datetime', 'lane', 'speed', 'length', 'class', 'gap', 'wrong_dir', 'display']
    areaname = 'Falen'
    
    processed_df = create_dataframe(path, widths, columns)
    sample = create_speed_list(processed_df, areaname)
    sample_tmp = read_sample(r"C:\Users\HP\Desktop\Anas\Research Paper\CURE\Codes\data_file_25r.txt")
    
    # run cure...
    n_clusters = 2
    n_rep = 15
    alpha = 0.1
    use_ccore = False
    
    cure_instance = cure(sample_tmp, n_clusters, n_rep, alpha, use_ccore)
    cure_instance.process()
    clusters = cure_instance.get_clusters()
    print("ALGORITHM SUCCESSFULLY COMPLETED.....")
    
# entry point for main script...
if __name__ == '__main__':
    main()