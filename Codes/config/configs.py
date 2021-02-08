MODEL_COLLAB = 'collaborative_filtering'
MODEL_CONTENT = 'content_based'
MODEL_HYBRID = 'hybrid_recommender'

interaction_weightages = {'content_watched': 1.0,'content_liked': 2.0, 'content_saved': 3.0, 'content_followed': 4.0,'content_commented_on': 5.0}
EVAL_RANDOM_SAMPLE_NON_INTERACTED_ITEMS = 100
country_name_map = {
    'AU': ('AUS', 'Australia'),
    'GB': ('GBR', 'United Kingdom'),
    'DE': ('DEU', 'Germany'),
    'CN': ('CHN', 'China'),
    'CL': ('CHL', 'Chile'),
    'NL': ('NLD', 'Netherlands'),
    'DE': ('DEU', 'Germany'),
    'IE': ('IRL', 'Ireland'),
    'IS': ('ISL', 'Iceland'),
    'SG': ('SGP', 'Singapure'),
    'AR': ('ARG', 'Argentina'),
    'PT': ('PRT', 'Portugal'),
    'IN': ('IND', 'India'),
    'BR': ('BRA', 'Brazil'),
    'US': ('USA', 'United States'),
    'KR': ('KOR', 'South Korea'),
    'CA': ('CAN', 'Canada'),
    'JP': ('JPN', 'Japan'),
    'ES': ('ESP', 'Spain'),
    'IT': ('ITA', 'Italy'),
    'MY': ('MYS', 'Malaysia'),
    'CO': ('COL', 'Colombia'),
}

#The number of factors to factor the user-item matrix.
NUMBER_OF_FACTORS_MF = 15