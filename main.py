#####################################   data importing and processing    ###########################################
# 1. Import the data from the csv file removing any rows that have no transcript data or that have the string "NA" for their transcript


"""
Utility:
Reads the data and cleans it, storing a list of words at each index of the dataframe
Returns:
the parsed data as a pandas dataframe
"""
def read_data():
    pass


"""
Utility:
turns a string into a cleaned list of words removing all punctuation numbers non-english characters and stop words
Returns:
A list of words
"""
def clean_parse_data():
    pass



#####################################   System Initialization    ####################################################


# 1. Requires some gui for allowing the user to select the genres that they are most interested in creating the user profile

# 2. Requires that the youtubers are all assigned a similarity score to each genre
# 2.1 Use the corpus of transcripts to generate word2vec embeddings then compare the vectors of each catergory name to the averaged w2v vectors of each youtuber
# 2.2 Create some normalized mapping of this similarity score of a transcript to a genre for each youtuber stored as a vector


"""
Utility:
Provide the user with a quiz like interface to score the genres that they are most interested in
Returns:
A user profile vector (or class) that stores the user's preferences
"""
def query_user():
    pass

"""
Utility:
Generates a vector of scores for different genres using the word2vec embeddings of the youtuber's transcripts
More specifically, the vector is the average of the word2vec embeddings of each word in the transcript
and the score is a normalized mapping from the cosine similarity of the genre name and the average transcript vector.
Should add the vectors as a new coloumn to the dataframe names "genre vectors"

This function should check if the youtuber genre vectors are already part of the preexisting data set and do nothing if they are

Parameters:
data - the dataframe of youtuber data

"""
def generate_youtuber_genre_vectors(data):
    pass


#####################################   System recommedations   ######################################################

# 1. Compute the system recommendations for each user by taking the dot product the user profile vector and the youtuber genre vectors
# 2. Use the top 10 scores to generate the recommendations for the user
# 3. Have the user select the youtubers amongst the list that they find the most interesting (could supply the links to each youtubers home page)

"""
Utility:
Computes the recommendations by taking the dot product of the user profile vector and the youtuber genre vectors returning the top n recommendations

Parameters:
user_profile - the user profile vector
n - the number of recommendations to generate
youtube_vectors - the dataframe of youtuber data

Returns:
top n recommendations
"""
def generate_recommendations(user_profile, youtuber_vectors, n):
    pass


"""
Utility:
Using the recommendations generated by the system, have the user select the youtubers that they find the most interesting

Parameters:
recommendations - the top n recommendations generated by the system

Returns:
the user's selected recommendations
"""
def select_recommendations(recommendations):
    pass


#####################################   Feedback    ##########################################################

# 1. Using the information gained from the user's recommendations, update the user profile vector to better reflect the user's interests
# 2. Repeat the recommendation process with the updated user profile vector

"""
Utility:
Using the selected Recommendations, update the user profile vector to better reflect the user's interests

Parameters:
user_profile - the user profile vector
selected_recommendations - the youtubers that the user selected as interesting

Returns:
updated user profile vector
"""
def update_user_profile(user_profile, selected_recommendations):
    pass




#####################################   System Evaluation    ##########################################################

# 1. Use the user's feedback to evaluate the system's performance (not sure how to do this yet but we should have built in evaluation metrics)


"""
Utility:
Provides a way to evaluate the system's performance by displaying evaluation metrics (Look back at what we said in our proposal)

Parameters:
recommendations - the top n recommendations generated by the system
selected_recommendations - the youtubers that the user selected as interesting
"""
def evaluate_system(recommendations, selected_recommendations):
    pass



#####################################  Shutdown ######################################################################
# 1. Save user preferences and youtuber genre vectors for next time the program is started

"""
Utility:
saves all of the computed data accordingly
"""
def shutdown():
    pass



##################################### Reach Goals that add complexity  ##########################################################

# make the system able to store user profiles between sessions
# make the system able to have multiple users
# utilize the multiple user data to include matrix factorization (aka collaborative filtering) to improve the system's recommendations



def main():
    pass




if __name__ == '__main__':
    main()