# -*- coding: utf-8 -*-
"""
Created on Mon May  4 17:19:53 2020

@author: Azadeh
"""

import pandas as pd

df = pd.read_csv('path_to_data')
df.head(10)



# Get column names
column_names = df.columns
print(column_names)
# Get column data types
df.dtypes
# Also check if the column is unique
for i in column_names:
  print('{} is unique: {}'.format(i, df[i].is_unique))
  
  
  
  # Check the index values
df.index.values
# Check if a certain index exists
'foo' in df.index.values
# If index does not exist
df.set_index('column_name_to_use', inplace=True)



# Create list comprehension of the columns you want to lose
columns_to_drop = [column_names[i] for i in [1, 3, 5]]
# Drop unwanted columns
df.drop(columns_to_drop, inplace=True, axis=1)



# Fill NaN with ' '
df['col'] = df['col'].fillna(' ')
# Fill NaN with 99
df['col'] = df['col'].fillna(99)
# Fill NaN with the mean of the column
df['col'] = df['col'].fillna(df['col'].mean())



df = pd.DataFrame(data={'col1':[np.nan, np.nan, 2,3,4, np.nan, np.nan]})
    col1
0   NaN
1   NaN
2   2.0
3   3.0
4   4.0 # This is the value to fill forward
5   NaN
6   NaN
df.fillna(method='pad', limit=1)
    col1
0   NaN
1   NaN
2   2.0
3   3.0
4   4.0
5   4.0 # Filled forward
6   NaN

# Fill the first two NaN values with the first available value
df.fillna(method='bfill')
    col1
0   2.0 # Filled
1   2.0 # Filled
2   2.0 
3   3.0
4   4.0
5   NaN
6   NaN



# Drop any rows which have any nans
df.dropna()
# Drop columns that have any nans
df.dropna(axis=1)
# Only drop columns which have at least 90% non-NaNs
df.dropna(thresh=int(df.shape[0] * .9), axis=1)


"""np.where(if_this_is_true, do_this, else_do_that)"""

# Follow this syntax
np.where(if_this_condition_is_true, do_this, else_this)
# Example
df['new_column'] = np.where(df[i] > 10, 'foo', 'bar) 

df['new_column'] = np.where(df['col'].str.startswith('foo') and  
                            not df['col'].str.endswith('bar'), 
                            True, 
                            df['col'])


# Three level nesting with np.where
np.where(if_this_condition_is_true_one, do_this, 
  np.where(if_this_condition_is_true_two, do_that, 
    np.where(if_this_condition_is_true_three, do_foo, do_bar)))
# A trivial example
df['foo'] = np.where(df['bar'] == 0, 'Zero',
              np.where(df['bar'] == 1, 'One',
                np.where(df['bar'] == 2, 'Two', 'Three')))



"""""""assert"""""""

assert(df['col1'] >= 0 ).all() # Should return nothing
assert(df['col1'] != str).any() # Should return nothing
assert(df['col1'] == df['col2']).all()

import pandas.util.testing as tm
tm.assert_series_equal(df['col1'], df['col2'])
>>
AssertionError: Series are different






