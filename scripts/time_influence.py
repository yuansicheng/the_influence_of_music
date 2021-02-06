import pandas as pd

raw_data_path = '../raw_data/'

def readInfluenceData(raw_data_path):
	print('in read_influence_data()')
	influence_data_path = raw_data_path + 'influence_data.csv'
	influence_data = pd.read_csv(influence_data_path)
	return influence_data

def getInfluencerId(influence_data):
	print('in getInfluencerId()')
	return list(influence_data['influencer_id'].unique())

def getFollowerId(influence_data):
	print('in getFollowerId()')
	return list(influence_data['follower_id'].unique())

def getMeanActiveStartByInfluencer(influence_data, out_file):
	print('in getMeanActiveStartByInfluencer()')
	influencers = getInfluencerId(influence_data)
	mean_active_start_by_influencer = []
	for influencer in influencers:
		mean_active_start_by_influencer.append( \
			influence_data[influence_data['influencer_id']==influencer]['follower_active_start'].mean()
		)
	result = {'influencer':influencers, 'mean_active_start_by_influencer':mean_active_start_by_influencer}
	result_df = pd.DataFrame(result)
	result_df.to_csv(out_file)
	return True
		

if __name__ == "__main__":
	influence_data = readInfluenceData(raw_data_path)
	#influencers = getInfluencerId(influence_data)
	getMeanActiveStartByInfluencer(influence_data, '../mean_active_start_by_influencer.csv')
	
	
