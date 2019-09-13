import pandas as pd

df = pd.read_csv('../input/severstal-steel-defect-detection/sample_submission.csv')
df.set_index('ImageId_ClassId', inplace=True)

df_submit = pd.read_csv('/kaggle/input/severstal_csv_submission/out.csv')
df_submit.set_index('ImageId_ClassId', inplace=True)

for name, row in df_submit.iterrows():
    df.loc[name] = row

df.reset_index(inplace=True)
df.to_csv('submission.csv', index=False)
