from LatentFactorModel import LatentFactorModel
from BaselineRecommendations import BaselineRecommendations
from DataPreprocessing import DataPreprocessing


if __name__ == '__main__':
    print "Welcome to the Anime Recommender System."

    #***************Data Preprocessing***************
    print "If this is your first time running the program? You'll need to create the necessary matrices and" \
          "remapped rating file if it is."
    user_input = raw_input("Create matrices and remapped rating file if they don't already exist? (yes or no) ")
    while user_input != 'yes' and user_input != 'no':
        user_input = raw_input("Create matrices and remapped rating file if they don't already exist? (yes or no) ")

    if user_input == 'yes':
        preprocess = DataPreprocessing()
        preprocess.run_random_split()
        preprocess.run_arbitrary_split()

    #***************Baseline Recommendation***************
    user_input = raw_input("Do you want to run the baseline recommendation? (yes or no) ")
    while user_input != 'yes' and user_input != 'no':
        user_input = raw_input("Do you want to run the baseline recommendation? (yes or no) ")
    if user_input == 'yes':
        user_input = raw_input("Do you want to run the randomly sampled data, arbitrarily sampled data or both? (r, a, b) ")
        while user_input != 'r' and user_input != 'a' and user_input != 'b':
            user_input = raw_input("Do you want to run the randomly sampled data, arbitrarily sampled data or both? (r, a, b) ")
        if user_input == 'r':
            print "Calculating RMSE for arbitrary dataset split."
            baseline = BaselineRecommendations('random')
            baseline = BaselineRecommendations('random')
            baseline.run_baseline()
        elif user_input == 'a':
            baseline = BaselineRecommendations('arbitrary')
            baseline.run_baseline()
        elif user_input == 'b':
            print "Calculating RMSE for random dataset split."
            baseline = BaselineRecommendations('random')
            baseline.run_baseline()
            print "Calculating RMSE for arbitrary dataset split."
            baseline = BaselineRecommendations('arbitrary')
            baseline.run_baseline()

    #***************Collaborative Filtering Recommendation***************




    #***************Latent Factor Model Recommendation***************
    run = raw_input("Do you want to run the latent factor model recommendation? (yes or no) ")
    while run != 'yes' and run != 'no':
        run = raw_input("Do you want to run the latent factor model recommendation? (yes or no) ")
    if run == 'yes':
        model_type = raw_input("Do you want to start a new model or load an old model? (old or new)\nWarning: "
                               "training a new model is very slow, it's recommended that you use the default model provided. ")
        while model_type != 'new' and model_type != 'old':
            model_type = raw_input("Do you want to start a new model or load an old model? (old or new) ")
        if model_type == 'new':
            parameters = raw_input("Do you want to use the default parameters? (yes or no) ")
            while parameters != 'yes' and parameters != 'no':
                parameters = raw_input("Do you want to use the default parameters? (yes or no) ")
            if parameters == 'yes':
                print "Initializing the latent factor model."
                latent_model = LatentFactorModel(epochs=15, k=10, learning_rate=0.006, lambda_reg=0.06)
                print "Beginning the long training process..."
                latent_model.run_new_model()
            elif parameters == 'no':
                epochs = input("Enter the number of epochs to train for: ")
                k = input("Enter the number of latent factors: ")
                learning_rate = input("Enter the learning rate: ")
                lambda_reg = input("Enter the lambda regularization value: ")
                print "Initializing the latent factor model."
                latent_model = LatentFactorModel(epochs=epochs, k=k, learning_rate=learning_rate, lambda_reg=lambda_reg)
                print "Beginning the long training process..."
                latent_model.run_new_model()
        elif model_type == 'old':
            default_model = raw_input("Do you want to load the default model? (yes or no)\nNote: it's recommended "
                                          "to load the default model. ")
            while default_model != 'yes' and default_model != 'no':
                default_model = raw_input("Do you want to load the default model? (yes or no)\nNote: it's recommended "
                                          "to load the default model. ")
            if default_model == 'yes':
                print "Initializing the latent factor model."
                latent_model = LatentFactorModel(epochs=50, k=10, learning_rate=0.006, lambda_reg=0.06)
                latent_model.load_model(model_directory='optimization/2017-11-23_16-28-35/')
                print "Calculating the random split test RMSE."
                test_rmse = latent_model.calculate_test_rmse()
                print "Random split test RMSE is: " + str(test_rmse)
            elif default_model == 'no':
                directory = raw_input("Enter the model directory (e.g. 'optimization/2017-11-23_16-28-35/'): ")
                print "Initializing the latent factor model."
                latent_model = LatentFactorModel(epochs=50, k=10, learning_rate=0.006, lambda_reg=0.06)
                latent_model.load_model(model_directory=directory)
                print "Calculating the random split test RMSE."
                test_rmse = latent_model.calculate_test_rmse()
                print "Random split test RMSE is: " + str(test_rmse)


    # Uncomment only one dataset
    # dataset = 'random'
    # dataset = 'arbitrary'

    # learning_rate_trials = [0.015, 0.006, 0.002]
    # lambda_reg_trials = [0.06, 0.02]
    # k_trials = [5, 10, 20]

    #start_whole = time.time()

    #recommender = RecommenderSystems(dataset=dataset)
    #recommender.initialize_program()

    # baseline = BaselineRecommendations(dataset)
    # baseline.run_baseline()
    #latent_model = LatentFactorModel(epochs=50, k=k_trials[2], learning_rate=learning_rate_trials[0], lambda_reg=lambda_reg_trials[0])

    # Overrides default parameters passed in constructor
    #latent_model.run_new_model()
    #latent_model.run_old_model(model_directory='optimization/2017-11-23_16-28-35/')

    #recommender.fill_similarity_matrix(centered_training_filepath, similarity_filepath)
    #recommender.collaborative_filter(similarity_filepath)

    #end = time.time()
    #print "Time to run program: " + str((end - start_whole))
