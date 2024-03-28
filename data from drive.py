# -*- coding: utf-8 -*-
"""
Create a data file where each raw is an increment of one meter of driving distance. 
"""
import numpy as np
import pandas as pd
import scipy.interpolate
import os

#Create a blank DF to collect the data into each time From the for loop
#df_ph_accumulated = pd.DataFrame()
#Latency is a file called calc.events.csv from the Readme folder from Ariel Uni Driv

files = pd.read_csv("C:\\Users\\LAB-ORENMUZ\\Desktop\\NaamaNicole\\calc_simulator_and_corresponding_physiological_filesN&N - Copy.csv")


files = files[pd.notnull(files["PreprocessFile"])]
#print(files)
#physiological = pd.read_csv("H:\My Drive\Ariel Uni\Readme\calc_pyhisiological_headers.csv")
#physiological = physiological[physiological["col"]=='HRV_HF']
#physiological=physiological.reset_index()
#files=files.merge(physiological,how="inner",on=['Id','triggered_by','Scenario','Condition'])
files=files.reset_index()
files = files.filter(items = ['Id', 'triggered_by','Scenario', 'Condition', 'PreprocessFile'])
files = files.drop_duplicates().reset_index(drop=True)
#files = files.reset_index()

#Scenarios=files["Scenario"].unique()


index = ['SimulationTime', 
         'ECG_Rate',
         'ECG_Rate_Mean',
         'ECG_Rate_Mean_5sec',
         'HRV_SDNN_5sec',
         'HRV_SDNN', 
         'HRV_HF',
         'HRV_LF',
         'HRV_LFHF',
         'PupilDiameter',
         'EDA_Tonic',
         'EDA_Phasic',
         
         'EDA_Phasic_Mean_5sec',
         'EDA_Phasic_sd_5sec',
         'HR_Mean_5sec',
         'SDNN_5sec',
         'PupilDiameter_Mean_5sec',
         'PupilDiameter_sd_5sec',
         
         'EDA_Phasic_Mean_1sec',
         'EDA_Phasic_sd_1sec',
         'HR_Mean_1sec',
         'SDNN_1sec',
         'PupilDiameter_Mean_1sec',
         'PupilDiameter_sd_1sec',
         'PupilDiameterBin1_Mean_1sec',
         'PupilDiameterBin2_Mean_1sec',
         'PupilDiameterBin3_Mean_1sec',
         
         'PupilDiameterBin1_Mean_5sec',
         'PupilDiameterBin2_Mean_5sec',
         'PupilDiameterBin3_Mean_5sec',
         
         'EEG12_ALPHA_Mean_1sec',
         'EEG12_BETA_Mean_1sec',
         'EEG12_THETA_Mean_1sec',
         
         'SCR_Events',
         'Speed','Latitude',
         
         'LateralAcceleration_Mean_1sec',
         'LateralAcceleration_sd_1sec',
         
         'ForwaredAcceleration_Mean_1sec',
         'ForwaredAcceleration_sd_1sec',
         
         'Longitude','DistanceToLead',
         'ForwaredAcceleration','LateralAcceleration']
def is_valide_file(fpath):  
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0


Scenarios=['Baseline']
for s in np.arange(len(Scenarios)):

    Scenario=Scenarios[s]
    Scenariofiles = files[files['Scenario']==Scenario]
    path_to_file="C:\\Users\\LAB-ORENMUZ\\Desktop\\NaamaNicole\\calc_by_distance_NEW_"+Scenario+".csv" 
    first_to_csv=1 ## flage
    print(Scenario)
    df_ph_accumulated = pd.DataFrame()
    result_df=pd.DataFrame()
    for i in range(len(Scenariofiles)):
        Id = Scenariofiles['Id'].iloc[i]
        print(Id)
        Condition = Scenariofiles['Condition'].iloc[i]
        triggered_by = Scenariofiles['triggered_by'].iloc[i]
        file = str(Scenariofiles ['PreprocessFile'].iloc[i])
        if is_valide_file(file):
            df = pd.read_csv(file) 
            df = df.dropna(subset=['MeasurementTime'])
            ### Additional parameters:
            Hz=1/np.median(np.diff(df['MeasurementTime']))
        
            ## replace ECG entries where heart rate<50 witn None
        
            if 'ECG_Rate' in df.columns:
                v=df['ECG_Rate']<50
                df.loc[v,['ECG_Rate_Mean','HRV_SDNN','HRV_RMSSD','HRV_LF','HRV_HF']]=None
        
            if 'ECG_Rate_Mean' in df.columns:
                v=df['ECG_Rate_Mean']<50
                df.loc[v,['ECG_Rate_Mean','HRV_SDNN','HRV_RMSSD','HRV_LF','HRV_HF']]=None
        
            if 'HRV_LF' in df.columns:
                df["HRV_LFHF"]= df["HRV_LF"]/ df["HRV_HF"]
        
            window_size=int(5*Hz) # window size is five seconds
            if 'EDA_Phasic' in df.columns:
                df['EDA_Phasic_Mean_5sec']= df['EDA_Phasic'].rolling(window_size,center=True,min_periods=1).mean() 
                df['EDA_Phasic_sd_5sec']= df['EDA_Phasic'].rolling(window_size,center=True,min_periods=1).std() 

            if 'ECG_Rate' in df.columns:
                df['HR_Mean_5sec']= 1/pd.DataFrame(1/df['ECG_Rate']).rolling(window_size,center=True,min_periods=1).mean() 
                df['SDNN_5sec']= pd.DataFrame(1/df['ECG_Rate']).rolling(window_size,center=True,min_periods=1).std()
        
            if 'PupilDiameter' in df.columns:
                df['PupilDiameter_Mean_5sec']= df['PupilDiameter'].rolling(window_size,center=True,min_periods=1).mean() 
                df['PupilDiameter_sd_5sec']= df['PupilDiameter'].rolling(window_size,center=True,min_periods=1).std()
            
            if 'PupilDiameterBin1' in df.columns:
                df['PupilDiameterBin1_Mean_5sec']= df['PupilDiameterBin1'].rolling(window_size,center=True,min_periods=1).mean() 
                df['PupilDiameterBin2_Mean_5sec']= df['PupilDiameterBin2'].rolling(window_size,center=True,min_periods=1).std()
                df['PupilDiameterBin3_Mean_5sec']= df['PupilDiameterBin3'].rolling(window_size,center=True,min_periods=1).std()
                      
            window_size=int(1*Hz) # window size is 1 seconds
            if 'EDA_Phasic' in df.columns:
                df['EDA_Phasic_Mean_1sec']= df['EDA_Phasic'].rolling(window_size,center=True,min_periods=1).mean() 
                df['EDA_Phasic_sd_1sec']= df['EDA_Phasic'].rolling(window_size,center=True,min_periods=1).std() 

            if 'ECG_Rate' in df.columns:
                df['HR_Mean_1sec']= 1/pd.DataFrame(1/df['ECG_Rate']).rolling(window_size,center=True,min_periods=1).mean() 
                df['SDNN_1sec']= pd.DataFrame(1/df['ECG_Rate']).rolling(window_size,center=True,min_periods=1).std()
                
            if 'PupilDiameter' in df.columns:
                df['PupilDiameter_Mean_1sec']= df['PupilDiameter'].rolling(window_size,center=True,min_periods=1).mean() 
                df['PupilDiameter_sd_1sec']= df['PupilDiameter'].rolling(window_size,center=True,min_periods=1).std()
                
            if 'PupilDiameterBin1' in df.columns:
                df['PupilDiameterBin1_Mean_1sec']= df['PupilDiameterBin1'].rolling(window_size,center=True,min_periods=1).mean() 
                df['PupilDiameterBin2_Mean_1sec']= df['PupilDiameterBin2'].rolling(window_size,center=True,min_periods=1).std()
                df['PupilDiameterBin3_Mean_1sec']= df['PupilDiameterBin3'].rolling(window_size,center=True,min_periods=1).std()
            
            for channel in range(1,12,1):
                if 'EEG'+str(channel)+'_BETA' in df.columns: 
                    df['EEG'+str(channel)+'_ALPHA_Mean_1sec']=df['EEG12_ALPHA'].rolling(window_size,center=True,min_periods=1).mean() 
                    df['EEG'+str(channel)+'_BETA_Mean_1sec']=df['EEG12_BETA'].rolling(window_size,center=True,min_periods=1).mean() 
                    df['EEG'+str(channel)+'_THETA_Mean_1sec']=df['EEG12_THETA'].rolling(window_size,center=True,min_periods=1).mean() 

            if 'LateralAcceleration' in df.columns:
                df['LateralAcceleration_Mean_1sec']= df['LateralAcceleration'].rolling(window_size,center=True,min_periods=1).mean() 
                df['LateralAcceleration_sd_1sec']= df['LateralAcceleration'].rolling(window_size,center=True,min_periods=1).std() 
        
            if 'ForwaredAcceleration' in df.columns:
                df['ForwaredAcceleration_Mean_1sec']= df['ForwaredAcceleration'].rolling(window_size,center=True,min_periods=1).mean() 
                df['ForwaredAcceleration_sd_1sec']= df['ForwaredAcceleration'].rolling(window_size,center=True,min_periods=1).std() 
                
    


            result_df = pd.concat([result_df, df], ignore_index=True)

            
        result_df.to_csv(path_to_file, index=False)    

