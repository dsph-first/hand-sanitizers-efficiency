import pandas as pd
import plotly.graph_objects as go
import yaml


def map_ratings_to_scale(ratings):
    rating_scale = {
        'Poor': 1,
        'Fair': 2,
        'Neutral': 3,
        'Good': 4,
        'Very Good': 5
    }
    mapped_ratings = []
    for rating in ratings:
        if isinstance(rating, (float, int)):
            mapped_ratings.append(rating)
        elif isinstance(rating, str):
            cleaned_rating = rating.strip().title()
            mapped_rating = rating_scale.get(cleaned_rating, 0)
            mapped_ratings.append(mapped_rating)
        else:
            mapped_ratings.append(0)
    return mapped_ratings


categories = data.columns[1:7].tolist()
categories += categories[:1]

fig = go.Figure()

individual_traces_indices = []

for index, row in data.iterrows():
    ratings = map_ratings_to_scale(row[1:].tolist())
    ratings += ratings[:1]
    
    trace = go.Scatterpolar(
        r=ratings,
        theta=categories,
        fill='toself',
        name=f'Participant {row["ID"]}',
        visible=False  
    )
    fig.add_trace(trace)
    individual_traces_indices.append(len(fig.data) - 1)

average_ratings = []
for category in data.columns[1:7]:
    category_ratings = map_ratings_to_scale(data[category].tolist())
    average_rating = sum(category_ratings) / len(category_ratings)
    average_ratings.append(average_rating)
average_ratings += average_ratings[:1]  

fig.add_trace(go.Scatterpolar(
    r=average_ratings,
    theta=categories,
    fill='toself',
    line_color='blue',
    name='Average Ratings'
))

fig.update_layout(
    updatemenus=[
        dict(
            buttons=[
                dict(label='Individual',
                     method='update',
                     args=[{'visible': [i in individual_traces_indices for i in range(len(fig.data))]},
                           {'title': 'Individual Ratings'}]),
                dict(label='Average',
                     method='update',
                     args=[{'visible': [False] * len(individual_traces_indices) + [True] * (len(fig.data) - len(individual_traces_indices))},
                           {'title': 'Average Ratings'}]),
            ],
            direction="down",
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.1,
            xanchor="left",
            y=1.1,
            yanchor="top"
        ),
    ]
)

fig.update_layout(
    title='Individual Ratings',
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0, 6],
            tickvals=[0, 1, 2, 3, 4, 5],
            ticktext=['', 'Poor', 'Fair', 'Neutral', 'Good', 'Very Good']
        )),
    showlegend=True
)

fig.show()
