"""create-exercises

Revision ID: 94e835e8242f
Revises: d7cf4089d422
Create Date: 2022-01-10 18:52:04.831978

"""
from alembic import op
from sqlalchemy.sql import table, column
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '94e835e8242f'
down_revision = 'd7cf4089d422'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'exercises',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('category', sa.String),
        sa.Column('primaryMuscles', sa.ARRAY(sa.String)),
        sa.Column('secondaryMuscles', sa.ARRAY(sa.String))
    )

    op.bulk_insert('exercises',
        [
            {
            "id": 0,
            "name": "3/4 Sit-Up",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 1,
            "name": "90/90 Hamstring",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves"],
            "category": "stretching"
            },
            {
            "id": 2,
            "name": "Ab Crunch Machine",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 3,
            "name": "Ab Roller",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["shoulders"],
            "category": "strength"
            },
            {
            "id": 4,
            "name": "Adductor",
            "primaryMuscles": ["adductors"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 5,
            "name": "Adductor/Groin",
            "primaryMuscles": ["adductors"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 6,
            "name": "Advanced Kettlebell Windmill",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["glutes", "hamstrings", "shoulders"],
            "category": "strength"
            },
            {
            "id": 7,
            "name": "Air Bike",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 8,
            "name": "All Fours Quad Stretch",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["quadriceps"],
            "category": "stretching"
            },
            {
            "id": 9,
            "name": "Alternate Hammer Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 10,
            "name": "Alternate Heel Touchers",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 11,
            "name": "Alternate Incline Dumbbell Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 12,
            "name": "Alternate Leg Diagonal Bound",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "abductors",
                "adductors",
                "calves",
                "glutes",
                "hamstrings"
            ],
            "category": "plyometrics"
            },
            {
            "id": 13,
            "name": "Alternating Cable Shoulder Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 14,
            "name": "Alternating Deltoid Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 15,
            "name": "Alternating Floor Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["abdominals", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 16,
            "name": "Alternating Hang Clean",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "biceps",
                "calves",
                "forearms",
                "glutes",
                "lower back",
                "traps"
            ],
            "category": "strength"
            },
            {
            "id": 17,
            "name": "Alternating Kettlebell Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 18,
            "name": "Alternating Kettlebell Row",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats"],
            "category": "strength"
            },
            {
            "id": 19,
            "name": "Alternating Renegade Row",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["abdominals", "biceps", "chest", "lats", "triceps"],
            "category": "strength"
            },
            {
            "id": 20,
            "name": "Ankle Circles",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 21,
            "name": "Ankle On The Knee",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 22,
            "name": "Anterior Tibialis-SMR",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 23,
            "name": "Anti-Gravity Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["middle back", "traps", "triceps"],
            "category": "strength"
            },
            {
            "id": 24,
            "name": "Arm Circles",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["traps"],
            "category": "stretching"
            },
            {
            "id": 25,
            "name": "Arnold Dumbbell Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 26,
            "name": "Around The Worlds",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders"],
            "category": "strength"
            },
            {
            "id": 27,
            "name": "Atlas Stone Trainer",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": [
                "biceps",
                "forearms",
                "glutes",
                "hamstrings",
                "quadriceps"
            ],
            "category": "strongman"
            },
            {
            "id": 28,
            "name": "Atlas Stones",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": [
                "abdominals",
                "adductors",
                "biceps",
                "calves",
                "forearms",
                "glutes",
                "hamstrings",
                "middle back",
                "quadriceps",
                "traps"
            ],
            "category": "strongman"
            },
            {
            "id": 29,
            "name": "Axle Deadlift",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": [
                "forearms",
                "glutes",
                "hamstrings",
                "middle back",
                "quadriceps",
                "traps"
            ],
            "category": "strongman"
            },
            {
            "id": 30,
            "name": "Back Flyes - With Bands",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["middle back", "triceps"],
            "category": "strength"
            },
            {
            "id": 31,
            "name": "Backward Drag",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "calves",
                "forearms",
                "glutes",
                "hamstrings",
                "lower back"
            ],
            "category": "strongman"
            },
            {
            "id": 32,
            "name": "Backward Medicine Ball Throw",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "plyometrics"
            },
            {
            "id": 33,
            "name": "Balance Board",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": ["hamstrings", "quadriceps"],
            "category": "strength"
            },
            {
            "id": 34,
            "name": "Ball Leg Curl",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves", "glutes"],
            "category": "strength"
            },
            {
            "id": 35,
            "name": "Band Assisted Pull-Up",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["abdominals", "forearms", "middle back"],
            "category": "strength"
            },
            {
            "id": 36,
            "name": "Band Good Morning",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["glutes", "lower back"],
            "category": "powerlifting"
            },
            {
            "id": 37,
            "name": "Band Good Morning (Pull Through)",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["glutes", "lower back"],
            "category": "powerlifting"
            },
            {
            "id": 38,
            "name": "Band Hip Adductions",
            "primaryMuscles": ["adductors"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 39,
            "name": "Band Pull Apart",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["middle back", "traps"],
            "category": "strength"
            },
            {
            "id": 40,
            "name": "Band Skull Crusher",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 41,
            "name": "Barbell Ab Rollout",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["lower back", "shoulders"],
            "category": "strength"
            },
            {
            "id": 42,
            "name": "Barbell Ab Rollout - On Knees",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["lower back", "shoulders"],
            "category": "strength"
            },
            {
            "id": 43,
            "name": "Barbell Bench Press - Medium Grip",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 44,
            "name": "Barbell Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 45,
            "name": "Barbell Curls Lying Against An Incline",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 46,
            "name": "Barbell Deadlift",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": [
                "calves",
                "forearms",
                "glutes",
                "hamstrings",
                "lats",
                "middle back",
                "quadriceps",
                "traps"
            ],
            "category": "strength"
            },
            {
            "id": 47,
            "name": "Barbell Full Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings", "lower back"],
            "category": "strength"
            },
            {
            "id": 48,
            "name": "Barbell Glute Bridge",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["calves", "hamstrings"],
            "category": "powerlifting"
            },
            {
            "id": 49,
            "name": "Barbell Guillotine Bench Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 50,
            "name": "Barbell Hack Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "forearms", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 51,
            "name": "Barbell Hip Thrust",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["calves", "hamstrings"],
            "category": "powerlifting"
            },
            {
            "id": 52,
            "name": "Barbell Incline Bench Press - Medium Grip",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 53,
            "name": "Barbell Incline Shoulder Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["chest"],
            "category": "strength"
            },
            {
            "id": 54,
            "name": "Barbell Lunge",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 55,
            "name": "Barbell Rear Delt Row",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["biceps", "lats", "middle back"],
            "category": "strength"
            },
            {
            "id": 56,
            "name": "Barbell Rollout from Bench",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["glutes", "hamstrings", "lats", "shoulders"],
            "category": "strength"
            },
            {
            "id": 57,
            "name": "Barbell Seated Calf Raise",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 58,
            "name": "Barbell Shoulder Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["chest", "triceps"],
            "category": "strength"
            },
            {
            "id": 59,
            "name": "Barbell Shrug",
            "primaryMuscles": ["traps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 60,
            "name": "Barbell Shrug Behind The Back",
            "primaryMuscles": ["traps"],
            "secondaryMuscles": ["forearms", "middle back"],
            "category": "strength"
            },
            {
            "id": 61,
            "name": "Barbell Side Bend",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["lower back"],
            "category": "strength"
            },
            {
            "id": 62,
            "name": "Barbell Side Split Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "hamstrings", "lower back"],
            "category": "strength"
            },
            {
            "id": 63,
            "name": "Barbell Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings", "lower back"],
            "category": "strength"
            },
            {
            "id": 64,
            "name": "Barbell Squat To A Bench",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings", "lower back"],
            "category": "strength"
            },
            {
            "id": 65,
            "name": "Barbell Step Ups",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings", "quadriceps"],
            "category": "strength"
            },
            {
            "id": 66,
            "name": "Barbell Walking Lunge",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 67,
            "name": "Battling Ropes",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["chest", "forearms"],
            "category": "strength"
            },
            {
            "id": 68,
            "name": "Bear Crawl Sled Drags",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strongman"
            },
            {
            "id": 69,
            "name": "Behind Head Chest Stretch",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders"],
            "category": "stretching"
            },
            {
            "id": 70,
            "name": "Bench Dips",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 71,
            "name": "Bench Jump",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "plyometrics"
            },
            {
            "id": 72,
            "name": "Bench Press - Powerlifting",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "forearms", "lats", "shoulders"],
            "category": "powerlifting"
            },
            {
            "id": 73,
            "name": "Bench Press - With Bands",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 74,
            "name": "Bench Press with Chains",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "lats", "shoulders"],
            "category": "powerlifting"
            },
            {
            "id": 75,
            "name": "Bench Sprint",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "plyometrics"
            },
            {
            "id": 76,
            "name": "Bent-Arm Barbell Pullover",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["chest", "lats", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 77,
            "name": "Bent-Arm Dumbbell Pullover",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["lats", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 78,
            "name": "Bent-Knee Hip Raise",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 79,
            "name": "Bent Over Barbell Row",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats", "shoulders"],
            "category": "strength"
            },
            {
            "id": 80,
            "name": "Bent Over Dumbbell Rear Delt Raise With Head On Bench",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 81,
            "name": "Bent Over Low-Pulley Side Lateral",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["lower back", "middle back", "traps"],
            "category": "strength"
            },
            {
            "id": 82,
            "name": "Bent Over One-Arm Long Bar Row",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats", "lower back", "traps"],
            "category": "strength"
            },
            {
            "id": 83,
            "name": "Bent Over Two-Arm Long Bar Row",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats"],
            "category": "strength"
            },
            {
            "id": 84,
            "name": "Bent Over Two-Dumbbell Row",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats", "shoulders"],
            "category": "strength"
            },
            {
            "id": 85,
            "name": "Bent Over Two-Dumbbell Row With Palms In",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats"],
            "category": "strength"
            },
            {
            "id": 86,
            "name": "Bent Press",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [
                "glutes",
                "hamstrings",
                "lower back",
                "quadriceps",
                "shoulders",
                "triceps"
            ],
            "category": "strength"
            },
            {
            "id": 87,
            "name": "Bicycling",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "cardio"
            },
            {
            "id": 88,
            "name": "Bicycling, Stationary",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "cardio"
            },
            {
            "id": 89,
            "name": "Board Press",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "forearms", "lats", "shoulders"],
            "category": "powerlifting"
            },
            {
            "id": 90,
            "name": "Body-Up",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["abdominals", "forearms"],
            "category": "strength"
            },
            {
            "id": 91,
            "name": "Body Tricep Press",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 92,
            "name": "Bodyweight Flyes",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["abdominals", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 93,
            "name": "Bodyweight Mid Row",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats"],
            "category": "strength"
            },
            {
            "id": 94,
            "name": "Bodyweight Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 95,
            "name": "Bodyweight Walking Lunge",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 96,
            "name": "Bosu Ball Cable Crunch With Side Bends",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 97,
            "name": "Bottoms-Up Clean From The Hang Position",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": ["biceps", "shoulders"],
            "category": "strength"
            },
            {
            "id": 98,
            "name": "Bottoms Up",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 99,
            "name": "Box Jump (Multiple Response)",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "abductors",
                "adductors",
                "calves",
                "glutes",
                "quadriceps"
            ],
            "category": "plyometrics"
            },
            {
            "id": 100,
            "name": "Box Skip",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "abductors",
                "adductors",
                "calves",
                "glutes",
                "quadriceps"
            ],
            "category": "plyometrics"
            },
            {
            "id": 101,
            "name": "Box Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "adductors",
                "calves",
                "glutes",
                "hamstrings",
                "lower back"
            ],
            "category": "powerlifting"
            },
            {
            "id": 102,
            "name": "Box Squat with Bands",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "abductors",
                "adductors",
                "calves",
                "glutes",
                "hamstrings",
                "lower back"
            ],
            "category": "powerlifting"
            },
            {
            "id": 103,
            "name": "Box Squat with Chains",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "abductors",
                "adductors",
                "calves",
                "glutes",
                "hamstrings",
                "lower back"
            ],
            "category": "strength"
            },
            {
            "id": 104,
            "name": "Brachialis-SMR",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 105,
            "name": "Bradford/Rocky Presses",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 106,
            "name": "Butt-Ups",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 107,
            "name": "Butt Lift (Bridge)",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["hamstrings"],
            "category": "strength"
            },
            {
            "id": 108,
            "name": "Butterfly",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 109,
            "name": "Cable Chest Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 110,
            "name": "Cable Crossover",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders"],
            "category": "strength"
            },
            {
            "id": 111,
            "name": "Cable Crunch",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 112,
            "name": "Cable Deadlifts",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["forearms", "glutes", "hamstrings", "lower back"],
            "category": "strength"
            },
            {
            "id": 113,
            "name": "Cable Hammer Curls - Rope Attachment",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 114,
            "name": "Cable Hip Adduction",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 115,
            "name": "Cable Incline Pushdown",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 116,
            "name": "Cable Incline Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 117,
            "name": "Cable Internal Rotation",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 118,
            "name": "Cable Iron Cross",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 119,
            "name": "Cable Judo Flip",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 120,
            "name": "Cable Lying Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 121,
            "name": "Cable One Arm Tricep Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 122,
            "name": "Cable Preacher Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 123,
            "name": "Cable Rear Delt Fly",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 124,
            "name": "Cable Reverse Crunch",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 125,
            "name": "Cable Rope Overhead Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 126,
            "name": "Cable Rope Rear-Delt Rows",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["biceps", "middle back"],
            "category": "strength"
            },
            {
            "id": 127,
            "name": "Cable Russian Twists",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 128,
            "name": "Cable Seated Crunch",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 129,
            "name": "Cable Seated Lateral Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["middle back", "traps"],
            "category": "strength"
            },
            {
            "id": 130,
            "name": "Cable Shoulder Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 131,
            "name": "Cable Shrugs",
            "primaryMuscles": ["traps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 132,
            "name": "Cable Wrist Curl",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 133,
            "name": "Calf-Machine Shoulder Shrug",
            "primaryMuscles": ["traps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 134,
            "name": "Calf Press",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 135,
            "name": "Calf Press On The Leg Press Machine",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 136,
            "name": "Calf Raise On A Dumbbell",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 137,
            "name": "Calf Raises - With Bands",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 138,
            "name": "Calf Stretch Elbows Against Wall",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 139,
            "name": "Calf Stretch Hands Against Wall",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 140,
            "name": "Calves-SMR",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 141,
            "name": "Car Deadlift",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "forearms",
                "glutes",
                "hamstrings",
                "lower back",
                "traps"
            ],
            "category": "strongman"
            },
            {
            "id": 142,
            "name": "Car Drivers",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 143,
            "name": "Carioca Quick Step",
            "primaryMuscles": ["adductors"],
            "secondaryMuscles": [
                "abdominals",
                "abductors",
                "calves",
                "glutes",
                "hamstrings",
                "quadriceps"
            ],
            "category": "plyometrics"
            },
            {
            "id": 144,
            "name": "Cat Stretch",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": ["middle back", "traps"],
            "category": "stretching"
            },
            {
            "id": 145,
            "name": "Catch and Overhead Throw",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["abdominals", "chest", "shoulders"],
            "category": "plyometrics"
            },
            {
            "id": 146,
            "name": "Chain Handle Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "powerlifting"
            },
            {
            "id": 147,
            "name": "Chain Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "powerlifting"
            },
            {
            "id": 148,
            "name": "Chair Leg Extended Stretch",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["adductors"],
            "category": "stretching"
            },
            {
            "id": 149,
            "name": "Chair Lower Back Stretch",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["lower back"],
            "category": "stretching"
            },
            {
            "id": 150,
            "name": "Chair Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 151,
            "name": "Chair Upper Body Stretch",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["biceps", "chest"],
            "category": "stretching"
            },
            {
            "id": 152,
            "name": "Chest And Front Of Shoulder Stretch",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders"],
            "category": "stretching"
            },
            {
            "id": 153,
            "name": "Chest Push (multiple response)",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["abdominals", "shoulders", "triceps"],
            "category": "plyometrics"
            },
            {
            "id": 154,
            "name": "Chest Push (single response)",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["abdominals", "shoulders", "triceps"],
            "category": "plyometrics"
            },
            {
            "id": 155,
            "name": "Chest Push from 3 point stance",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["abdominals", "shoulders", "triceps"],
            "category": "plyometrics"
            },
            {
            "id": 156,
            "name": "Chest Push with Run Release",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["abdominals", "shoulders", "triceps"],
            "category": "plyometrics"
            },
            {
            "id": 157,
            "name": "Chest Stretch on Stability Ball",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 158,
            "name": "Child's Pose",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": ["glutes", "middle back"],
            "category": "stretching"
            },
            {
            "id": 159,
            "name": "Chin-Up",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "forearms", "middle back"],
            "category": "strength"
            },
            {
            "id": 160,
            "name": "Chin To Chest Stretch",
            "primaryMuscles": ["neck"],
            "secondaryMuscles": ["traps"],
            "category": "stretching"
            },
            {
            "id": 161,
            "name": "Circus Bell",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [
                "forearms",
                "glutes",
                "hamstrings",
                "lower back",
                "traps",
                "triceps"
            ],
            "category": "strongman"
            },
            {
            "id": 162,
            "name": "Clean",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "calves",
                "forearms",
                "glutes",
                "lower back",
                "quadriceps",
                "shoulders",
                "traps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 163,
            "name": "Clean Deadlift",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "forearms",
                "glutes",
                "lower back",
                "middle back",
                "quadriceps",
                "traps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 164,
            "name": "Clean Pull",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "forearms",
                "glutes",
                "hamstrings",
                "lower back",
                "traps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 165,
            "name": "Clean Shrug",
            "primaryMuscles": ["traps"],
            "secondaryMuscles": ["forearms", "shoulders"],
            "category": "olympic weightlifting"
            },
            {
            "id": 166,
            "name": "Clean and Jerk",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [
                "abdominals",
                "glutes",
                "hamstrings",
                "lower back",
                "quadriceps",
                "traps",
                "triceps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 167,
            "name": "Clean and Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [
                "abdominals",
                "calves",
                "glutes",
                "hamstrings",
                "lower back",
                "middle back",
                "quadriceps",
                "shoulders",
                "traps",
                "triceps"
            ],
            "category": "strength"
            },
            {
            "id": 168,
            "name": "Clean from Blocks",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "calves",
                "glutes",
                "hamstrings",
                "shoulders",
                "traps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 169,
            "name": "Clock Push-Up",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 170,
            "name": "Close-Grip Barbell Bench Press",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 171,
            "name": "Close-Grip Dumbbell Press",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 172,
            "name": "Close-Grip EZ-Bar Curl with Band",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 173,
            "name": "Close-Grip EZ-Bar Press",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 174,
            "name": "Close-Grip EZ Bar Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 175,
            "name": "Close-Grip Front Lat Pulldown",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "middle back", "shoulders"],
            "category": "strength"
            },
            {
            "id": 176,
            "name": "Close-Grip Push-Up off of a Dumbbell",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["abdominals", "chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 177,
            "name": "Close-Grip Standing Barbell Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 178,
            "name": "Cocoons",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 179,
            "name": "Conan's Wheel",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "abdominals",
                "biceps",
                "calves",
                "forearms",
                "lower back",
                "shoulders",
                "traps"
            ],
            "category": "strongman"
            },
            {
            "id": 180,
            "name": "Concentration Curls",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 181,
            "name": "Cross-Body Crunch",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 182,
            "name": "Cross Body Hammer Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 183,
            "name": "Cross Over - With Bands",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["biceps", "shoulders"],
            "category": "strength"
            },
            {
            "id": 184,
            "name": "Crossover Reverse Lunge",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": [
                "abdominals",
                "abductors",
                "glutes",
                "hamstrings",
                "quadriceps"
            ],
            "category": "stretching"
            },
            {
            "id": 185,
            "name": "Crucifix",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["forearms"],
            "category": "strongman"
            },
            {
            "id": 186,
            "name": "Crunch - Hands Overhead",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 187,
            "name": "Crunch - Legs On Exercise Ball",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 188,
            "name": "Crunches",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 189,
            "name": "Cuban Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["traps"],
            "category": "strength"
            },
            {
            "id": 190,
            "name": "Dancer's Stretch",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": ["abductors", "glutes"],
            "category": "stretching"
            },
            {
            "id": 191,
            "name": "Dead Bug",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 192,
            "name": "Deadlift with Bands",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": [
                "forearms",
                "glutes",
                "hamstrings",
                "middle back",
                "quadriceps",
                "traps"
            ],
            "category": "powerlifting"
            },
            {
            "id": 193,
            "name": "Deadlift with Chains",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": [
                "forearms",
                "glutes",
                "hamstrings",
                "middle back",
                "quadriceps",
                "traps"
            ],
            "category": "powerlifting"
            },
            {
            "id": 194,
            "name": "Decline Barbell Bench Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 195,
            "name": "Decline Close-Grip Bench To Skull Crusher",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 196,
            "name": "Decline Crunch",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 197,
            "name": "Decline Dumbbell Bench Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 198,
            "name": "Decline Dumbbell Flyes",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 199,
            "name": "Decline Dumbbell Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 200,
            "name": "Decline EZ Bar Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 201,
            "name": "Decline Oblique Crunch",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 202,
            "name": "Decline Push-Up",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 203,
            "name": "Decline Reverse Crunch",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 204,
            "name": "Decline Smith Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 205,
            "name": "Deficit Deadlift",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": [
                "forearms",
                "glutes",
                "hamstrings",
                "middle back",
                "quadriceps",
                "traps"
            ],
            "category": "powerlifting"
            },
            {
            "id": 206,
            "name": "Depth Jump Leap",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "abductors",
                "adductors",
                "calves",
                "glutes",
                "hamstrings"
            ],
            "category": "plyometrics"
            },
            {
            "id": 207,
            "name": "Dip Machine",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 208,
            "name": "Dips - Chest Version",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 209,
            "name": "Dips - Triceps Version",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 210,
            "name": "Donkey Calf Raises",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 211,
            "name": "Double Kettlebell Alternating Hang Clean",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "biceps",
                "calves",
                "forearms",
                "glutes",
                "lower back",
                "quadriceps",
                "traps"
            ],
            "category": "strength"
            },
            {
            "id": 212,
            "name": "Double Kettlebell Jerk",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["calves", "quadriceps", "triceps"],
            "category": "strength"
            },
            {
            "id": 213,
            "name": "Double Kettlebell Push Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["calves", "quadriceps", "triceps"],
            "category": "strength"
            },
            {
            "id": 214,
            "name": "Double Kettlebell Snatch",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["glutes", "hamstrings", "quadriceps"],
            "category": "strength"
            },
            {
            "id": 215,
            "name": "Double Kettlebell Windmill",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["glutes", "hamstrings", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 216,
            "name": "Double Leg Butt Kick",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "abductors",
                "adductors",
                "calves",
                "glutes",
                "hamstrings"
            ],
            "category": "plyometrics"
            },
            {
            "id": 217,
            "name": "Downward Facing Balance",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["abdominals", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 218,
            "name": "Drag Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 219,
            "name": "Drop Push",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "plyometrics"
            },
            {
            "id": 220,
            "name": "Dumbbell Alternate Bicep Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 221,
            "name": "Dumbbell Bench Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 222,
            "name": "Dumbbell Bench Press with Neutral Grip",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 223,
            "name": "Dumbbell Bicep Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 224,
            "name": "Dumbbell Clean",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "calves",
                "forearms",
                "glutes",
                "lower back",
                "quadriceps",
                "shoulders",
                "traps"
            ],
            "category": "strength"
            },
            {
            "id": 225,
            "name": "Dumbbell Floor Press",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "powerlifting"
            },
            {
            "id": 226,
            "name": "Dumbbell Flyes",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 227,
            "name": "Dumbbell Incline Row",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "forearms", "lats", "shoulders"],
            "category": "strength"
            },
            {
            "id": 228,
            "name": "Dumbbell Incline Shoulder Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 229,
            "name": "Dumbbell Lunges",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 230,
            "name": "Dumbbell Lying One-Arm Rear Lateral Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["middle back"],
            "category": "strength"
            },
            {
            "id": 231,
            "name": "Dumbbell Lying Pronation",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 232,
            "name": "Dumbbell Lying Rear Lateral Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 233,
            "name": "Dumbbell Lying Supination",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 234,
            "name": "Dumbbell One-Arm Shoulder Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 235,
            "name": "Dumbbell One-Arm Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 236,
            "name": "Dumbbell One-Arm Upright Row",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["biceps", "traps"],
            "category": "strength"
            },
            {
            "id": 237,
            "name": "Dumbbell Prone Incline Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 238,
            "name": "Dumbbell Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["biceps"],
            "category": "strength"
            },
            {
            "id": 239,
            "name": "Dumbbell Rear Lunge",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 240,
            "name": "Dumbbell Scaption",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["traps"],
            "category": "strength"
            },
            {
            "id": 241,
            "name": "Dumbbell Seated Box Jump",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "plyometrics"
            },
            {
            "id": 242,
            "name": "Dumbbell Seated One-Leg Calf Raise",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 243,
            "name": "Dumbbell Shoulder Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 244,
            "name": "Dumbbell Shrug",
            "primaryMuscles": ["traps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 245,
            "name": "Dumbbell Side Bend",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 246,
            "name": "Dumbbell Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings", "lower back"],
            "category": "strength"
            },
            {
            "id": 247,
            "name": "Dumbbell Squat To A Bench",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings", "lower back"],
            "category": "strength"
            },
            {
            "id": 248,
            "name": "Dumbbell Step Ups",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 249,
            "name": "Dumbbell Tricep Extension -Pronated Grip",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 250,
            "name": "Dynamic Back Stretch",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 251,
            "name": "Dynamic Chest Stretch",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["middle back"],
            "category": "stretching"
            },
            {
            "id": 252,
            "name": "EZ-Bar Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 253,
            "name": "EZ-Bar Skullcrusher",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 254,
            "name": "Elbow Circles",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["traps"],
            "category": "stretching"
            },
            {
            "id": 255,
            "name": "Elbow to Knee",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 256,
            "name": "Elbows Back",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders"],
            "category": "stretching"
            },
            {
            "id": 257,
            "name": "Elevated Back Lunge",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 258,
            "name": "Elevated Cable Rows",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["middle back", "traps"],
            "category": "strength"
            },
            {
            "id": 259,
            "name": "Elliptical Trainer",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "cardio"
            },
            {
            "id": 260,
            "name": "Exercise Ball Crunch",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 261,
            "name": "Exercise Ball Pull-In",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 262,
            "name": "Extended Range One-Arm Kettlebell Floor Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 263,
            "name": "External Rotation",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 264,
            "name": "External Rotation with Band",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 265,
            "name": "External Rotation with Cable",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 266,
            "name": "Face Pull",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["middle back"],
            "category": "strength"
            },
            {
            "id": 267,
            "name": "Farmer's Walk",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [
                "abdominals",
                "glutes",
                "hamstrings",
                "lower back",
                "quadriceps",
                "traps"
            ],
            "category": "strongman"
            },
            {
            "id": 268,
            "name": "Fast Skipping",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "abductors",
                "adductors",
                "calves",
                "glutes",
                "hamstrings"
            ],
            "category": "plyometrics"
            },
            {
            "id": 269,
            "name": "Finger Curls",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 270,
            "name": "Flat Bench Cable Flyes",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 271,
            "name": "Flat Bench Leg Pull-In",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 272,
            "name": "Flat Bench Lying Leg Raise",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 273,
            "name": "Flexor Incline Dumbbell Curls",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 274,
            "name": "Floor Glute-Ham Raise",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves", "glutes"],
            "category": "strength"
            },
            {
            "id": 275,
            "name": "Floor Press",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "powerlifting"
            },
            {
            "id": 276,
            "name": "Floor Press with Chains",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "powerlifting"
            },
            {
            "id": 277,
            "name": "Flutter Kicks",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["hamstrings"],
            "category": "strength"
            },
            {
            "id": 278,
            "name": "Foot-SMR",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 279,
            "name": "Forward Drag with Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": [
                "calves",
                "glutes",
                "hamstrings",
                "quadriceps",
                "shoulders",
                "triceps"
            ],
            "category": "strongman"
            },
            {
            "id": 280,
            "name": "Frankenstein Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["abdominals", "calves", "glutes", "hamstrings"],
            "category": "olympic weightlifting"
            },
            {
            "id": 281,
            "name": "Freehand Jump Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 282,
            "name": "Frog Hops",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "stretching"
            },
            {
            "id": 283,
            "name": "Frog Sit-Ups",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 284,
            "name": "Front Barbell Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 285,
            "name": "Front Barbell Squat To A Bench",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 286,
            "name": "Front Box Jump",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "abductors",
                "adductors",
                "calves",
                "glutes",
                "quadriceps"
            ],
            "category": "plyometrics"
            },
            {
            "id": 287,
            "name": "Front Cable Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 288,
            "name": "Front Cone Hops (or hurdle hops)",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "abductors",
                "adductors",
                "calves",
                "glutes",
                "hamstrings"
            ],
            "category": "plyometrics"
            },
            {
            "id": 289,
            "name": "Front Dumbbell Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 290,
            "name": "Front Incline Dumbbell Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 291,
            "name": "Front Leg Raises",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 292,
            "name": "Front Plate Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 293,
            "name": "Front Raise And Pullover",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["lats", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 294,
            "name": "Front Squat (Clean Grip)",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["abdominals", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 295,
            "name": "Front Squats With Two Kettlebells",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes"],
            "category": "strength"
            },
            {
            "id": 296,
            "name": "Front Two-Dumbbell Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 297,
            "name": "Full Range-Of-Motion Lat Pulldown",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "middle back", "shoulders"],
            "category": "strength"
            },
            {
            "id": 298,
            "name": "Gironda Sternum Chins",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "middle back"],
            "category": "strength"
            },
            {
            "id": 299,
            "name": "Glute Ham Raise",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves", "glutes"],
            "category": "powerlifting"
            },
            {
            "id": 300,
            "name": "Glute Kickback",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["hamstrings"],
            "category": "strength"
            },
            {
            "id": 301,
            "name": "Goblet Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings", "shoulders"],
            "category": "strength"
            },
            {
            "id": 302,
            "name": "Good Morning",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["abdominals", "glutes", "lower back"],
            "category": "powerlifting"
            },
            {
            "id": 303,
            "name": "Good Morning off Pins",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["abdominals", "glutes", "lower back"],
            "category": "powerlifting"
            },
            {
            "id": 304,
            "name": "Gorilla Chin/Crunch",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["biceps", "lats"],
            "category": "strength"
            },
            {
            "id": 305,
            "name": "Groin and Back Stretch",
            "primaryMuscles": ["adductors"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 306,
            "name": "Groiners",
            "primaryMuscles": ["adductors"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 307,
            "name": "Hack Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 308,
            "name": "Hammer Curls",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 309,
            "name": "Hammer Grip Incline DB Bench Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 310,
            "name": "Hamstring-SMR",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 311,
            "name": "Hamstring Stretch",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 312,
            "name": "Handstand Push-Ups",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 313,
            "name": "Hang Clean",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "calves",
                "forearms",
                "glutes",
                "hamstrings",
                "lower back",
                "shoulders",
                "traps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 314,
            "name": "Hang Clean - Below the Knees",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "calves",
                "forearms",
                "glutes",
                "hamstrings",
                "lower back",
                "shoulders",
                "traps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 315,
            "name": "Hang Snatch",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "abdominals",
                "calves",
                "forearms",
                "glutes",
                "lower back",
                "quadriceps",
                "shoulders",
                "traps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 316,
            "name": "Hang Snatch - Below Knees",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "abdominals",
                "calves",
                "forearms",
                "glutes",
                "lower back",
                "quadriceps",
                "shoulders",
                "traps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 317,
            "name": "Hanging Bar Good Morning",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["abdominals", "glutes", "lower back"],
            "category": "powerlifting"
            },
            {
            "id": 318,
            "name": "Hanging Leg Raise",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 319,
            "name": "Hanging Pike",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 320,
            "name": "Heaving Snatch Balance",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "abdominals",
                "forearms",
                "glutes",
                "hamstrings",
                "shoulders",
                "triceps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 321,
            "name": "Heavy Bag Thrust",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["abdominals", "shoulders", "triceps"],
            "category": "plyometrics"
            },
            {
            "id": 322,
            "name": "High Cable Curls",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 323,
            "name": "Hip Circles (prone)",
            "primaryMuscles": ["abductors"],
            "secondaryMuscles": ["adductors"],
            "category": "stretching"
            },
            {
            "id": 324,
            "name": "Hip Extension with Bands",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["hamstrings"],
            "category": "strength"
            },
            {
            "id": 325,
            "name": "Hip Flexion with Band",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 326,
            "name": "Hip Lift with Band",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["calves", "hamstrings"],
            "category": "powerlifting"
            },
            {
            "id": 327,
            "name": "Hug A Ball",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": ["calves", "glutes"],
            "category": "stretching"
            },
            {
            "id": 328,
            "name": "Hug Knees To Chest",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": ["glutes"],
            "category": "stretching"
            },
            {
            "id": 329,
            "name": "Hurdle Hops",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "abductors",
                "adductors",
                "calves",
                "glutes",
                "hamstrings"
            ],
            "category": "plyometrics"
            },
            {
            "id": 330,
            "name": "Hyperextensions (Back Extensions)",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": ["glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 331,
            "name": "Hyperextensions With No Hyperextension Bench",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": ["glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 332,
            "name": "IT Band and Glute Stretch",
            "primaryMuscles": ["abductors"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 333,
            "name": "Iliotibial Tract-SMR",
            "primaryMuscles": ["abductors"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 334,
            "name": "Inchworm",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 335,
            "name": "Incline Barbell Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 336,
            "name": "Incline Bench Pull",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["lats", "shoulders"],
            "category": "strength"
            },
            {
            "id": 337,
            "name": "Incline Cable Chest Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 338,
            "name": "Incline Cable Flye",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders"],
            "category": "strength"
            },
            {
            "id": 339,
            "name": "Incline Dumbbell Bench With Palms Facing In",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 340,
            "name": "Incline Dumbbell Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 341,
            "name": "Incline Dumbbell Flyes",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders"],
            "category": "strength"
            },
            {
            "id": 342,
            "name": "Incline Dumbbell Flyes - With A Twist",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders"],
            "category": "strength"
            },
            {
            "id": 343,
            "name": "Incline Dumbbell Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 344,
            "name": "Incline Hammer Curls",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 345,
            "name": "Incline Inner Biceps Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 346,
            "name": "Incline Push-Up",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 347,
            "name": "Incline Push-Up Close-Grip",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 348,
            "name": "Incline Push-Up Depth Jump",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "plyometrics"
            },
            {
            "id": 349,
            "name": "Incline Push-Up Medium",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["abdominals", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 350,
            "name": "Incline Push-Up Reverse Grip",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["abdominals", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 351,
            "name": "Incline Push-Up Wide",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["abdominals", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 352,
            "name": "Intermediate Groin Stretch",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 353,
            "name": "Intermediate Hip Flexor and Quad Stretch",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 354,
            "name": "Internal Rotation with Band",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 355,
            "name": "Inverted Row",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["lats"],
            "category": "strength"
            },
            {
            "id": 356,
            "name": "Inverted Row with Straps",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats"],
            "category": "strength"
            },
            {
            "id": 357,
            "name": "Iron Cross",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [
                "chest",
                "glutes",
                "hamstrings",
                "lower back",
                "quadriceps",
                "traps"
            ],
            "category": "strength"
            },
            {
            "id": 358,
            "name": "Iron Crosses (stretch)",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 359,
            "name": "Isometric Chest Squeezes",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "plyometrics"
            },
            {
            "id": 360,
            "name": "Isometric Neck Exercise - Front And Back",
            "primaryMuscles": ["neck"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 361,
            "name": "Isometric Neck Exercise - Sides",
            "primaryMuscles": ["neck"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 362,
            "name": "Isometric Wipers",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["abdominals", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 363,
            "name": "JM Press",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 364,
            "name": "Jackknife Sit-Up",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 365,
            "name": "Janda Sit-Up",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 366,
            "name": "Jefferson Squats",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "calves",
                "glutes",
                "hamstrings",
                "lower back",
                "traps"
            ],
            "category": "strength"
            },
            {
            "id": 367,
            "name": "Jerk Balance",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["glutes", "hamstrings", "quadriceps", "triceps"],
            "category": "olympic weightlifting"
            },
            {
            "id": 368,
            "name": "Jerk Dip Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["abdominals", "calves"],
            "category": "olympic weightlifting"
            },
            {
            "id": 369,
            "name": "Jogging, Treadmill",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["glutes", "hamstrings"],
            "category": "cardio"
            },
            {
            "id": 370,
            "name": "Keg Load",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": [
                "abdominals",
                "biceps",
                "calves",
                "forearms",
                "glutes",
                "hamstrings",
                "middle back",
                "quadriceps",
                "shoulders",
                "traps"
            ],
            "category": "strongman"
            },
            {
            "id": 371,
            "name": "Kettlebell Arnold Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 372,
            "name": "Kettlebell Dead Clean",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "calves",
                "glutes",
                "lower back",
                "quadriceps",
                "traps"
            ],
            "category": "strength"
            },
            {
            "id": 373,
            "name": "Kettlebell Figure 8",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["hamstrings", "shoulders"],
            "category": "strength"
            },
            {
            "id": 374,
            "name": "Kettlebell Hang Clean",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "calves",
                "glutes",
                "lower back",
                "shoulders",
                "traps"
            ],
            "category": "strength"
            },
            {
            "id": 375,
            "name": "Kettlebell One-Legged Deadlift",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["glutes", "lower back"],
            "category": "strength"
            },
            {
            "id": 376,
            "name": "Kettlebell Pass Between The Legs",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["glutes", "hamstrings", "shoulders"],
            "category": "strength"
            },
            {
            "id": 377,
            "name": "Kettlebell Pirate Ships",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["abdominals"],
            "category": "strength"
            },
            {
            "id": 378,
            "name": "Kettlebell Pistol Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings", "shoulders"],
            "category": "strength"
            },
            {
            "id": 379,
            "name": "Kettlebell Seated Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 380,
            "name": "Kettlebell Seesaw Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 381,
            "name": "Kettlebell Sumo High Pull",
            "primaryMuscles": ["traps"],
            "secondaryMuscles": [
                "adductors",
                "glutes",
                "hamstrings",
                "quadriceps",
                "shoulders"
            ],
            "category": "strength"
            },
            {
            "id": 382,
            "name": "Kettlebell Thruster",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["quadriceps", "triceps"],
            "category": "strength"
            },
            {
            "id": 383,
            "name": "Kettlebell Turkish Get-Up (Lunge style)",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["abdominals", "hamstrings", "quadriceps", "triceps"],
            "category": "strength"
            },
            {
            "id": 384,
            "name": "Kettlebell Turkish Get-Up (Squat style)",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [
                "abdominals",
                "calves",
                "hamstrings",
                "quadriceps",
                "triceps"
            ],
            "category": "strength"
            },
            {
            "id": 385,
            "name": "Kettlebell Windmill",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["glutes", "hamstrings", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 386,
            "name": "Kipping Muscle Up",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": [
                "abdominals",
                "biceps",
                "forearms",
                "middle back",
                "shoulders",
                "traps",
                "triceps"
            ],
            "category": "strength"
            },
            {
            "id": 387,
            "name": "Knee Across The Body",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["abductors", "lower back"],
            "category": "stretching"
            },
            {
            "id": 388,
            "name": "Knee Circles",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": ["hamstrings", "quadriceps"],
            "category": "stretching"
            },
            {
            "id": 389,
            "name": "Knee/Hip Raise On Parallel Bars",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 390,
            "name": "Knee Tuck Jump",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "abductors",
                "adductors",
                "calves",
                "glutes",
                "quadriceps"
            ],
            "category": "plyometrics"
            },
            {
            "id": 391,
            "name": "Kneeling Arm Drill",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["abdominals"],
            "category": "plyometrics"
            },
            {
            "id": 392,
            "name": "Kneeling Cable Crunch With Alternating Oblique Twists",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 393,
            "name": "Kneeling Cable Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 394,
            "name": "Kneeling Forearm Stretch",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 395,
            "name": "Kneeling High Pulley Row",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "middle back"],
            "category": "strength"
            },
            {
            "id": 396,
            "name": "Kneeling Hip Flexor",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["quadriceps"],
            "category": "stretching"
            },
            {
            "id": 397,
            "name": "Kneeling Jump Squat",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["calves", "hamstrings", "quadriceps"],
            "category": "olympic weightlifting"
            },
            {
            "id": 398,
            "name": "Kneeling Single-Arm High Pulley Row",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "middle back"],
            "category": "strength"
            },
            {
            "id": 399,
            "name": "Kneeling Squat",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["abdominals", "hamstrings", "lower back"],
            "category": "powerlifting"
            },
            {
            "id": 400,
            "name": "Landmine 180's",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["glutes", "lower back", "shoulders"],
            "category": "strength"
            },
            {
            "id": 401,
            "name": "Landmine Linear Jammer",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [
                "abdominals",
                "calves",
                "chest",
                "hamstrings",
                "quadriceps",
                "triceps"
            ],
            "category": "strength"
            },
            {
            "id": 402,
            "name": "Lateral Bound",
            "primaryMuscles": ["adductors"],
            "secondaryMuscles": [
                "abductors",
                "calves",
                "glutes",
                "hamstrings",
                "quadriceps"
            ],
            "category": "plyometrics"
            },
            {
            "id": 403,
            "name": "Lateral Box Jump",
            "primaryMuscles": ["adductors"],
            "secondaryMuscles": [
                "abductors",
                "calves",
                "glutes",
                "hamstrings",
                "quadriceps"
            ],
            "category": "plyometrics"
            },
            {
            "id": 404,
            "name": "Lateral Cone Hops",
            "primaryMuscles": ["adductors"],
            "secondaryMuscles": [
                "abductors",
                "calves",
                "glutes",
                "hamstrings",
                "quadriceps"
            ],
            "category": "plyometrics"
            },
            {
            "id": 405,
            "name": "Lateral Raise - With Bands",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 406,
            "name": "Latissimus Dorsi-SMR",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 407,
            "name": "Leg-Over Floor Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 408,
            "name": "Leg-Up Hamstring Stretch",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 409,
            "name": "Leg Extensions",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 410,
            "name": "Leg Lift",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["hamstrings"],
            "category": "strength"
            },
            {
            "id": 411,
            "name": "Leg Press",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 412,
            "name": "Leg Pull-In",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 413,
            "name": "Leverage Chest Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 414,
            "name": "Leverage Deadlift",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 415,
            "name": "Leverage Decline Chest Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 416,
            "name": "Leverage High Row",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["lats"],
            "category": "strength"
            },
            {
            "id": 417,
            "name": "Leverage Incline Chest Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 418,
            "name": "Leverage Iso Row",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "middle back"],
            "category": "strength"
            },
            {
            "id": 419,
            "name": "Leverage Shoulder Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 420,
            "name": "Leverage Shrug",
            "primaryMuscles": ["traps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 421,
            "name": "Linear 3-Part Start Technique",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves", "quadriceps"],
            "category": "plyometrics"
            },
            {
            "id": 422,
            "name": "Linear Acceleration Wall Drill",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves", "glutes", "quadriceps"],
            "category": "plyometrics"
            },
            {
            "id": 423,
            "name": "Linear Depth Jump",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "plyometrics"
            },
            {
            "id": 424,
            "name": "Log Lift",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [
                "abdominals",
                "chest",
                "glutes",
                "hamstrings",
                "lower back",
                "middle back",
                "quadriceps",
                "traps",
                "triceps"
            ],
            "category": "strongman"
            },
            {
            "id": 425,
            "name": "London Bridges",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "forearms", "middle back"],
            "category": "strength"
            },
            {
            "id": 426,
            "name": "Looking At Ceiling",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 427,
            "name": "Low Cable Crossover",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders"],
            "category": "strength"
            },
            {
            "id": 428,
            "name": "Low Cable Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 429,
            "name": "Low Pulley Row To Neck",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["biceps", "middle back", "traps"],
            "category": "strength"
            },
            {
            "id": 430,
            "name": "Lower Back-SMR",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 431,
            "name": "Lower Back Curl",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 432,
            "name": "Lunge Pass Through",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves", "glutes", "quadriceps"],
            "category": "strength"
            },
            {
            "id": 433,
            "name": "Lunge Sprint",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 434,
            "name": "Lying Bent Leg Groin",
            "primaryMuscles": ["adductors"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 435,
            "name": "Lying Cable Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 436,
            "name": "Lying Cambered Barbell Row",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats", "traps"],
            "category": "strength"
            },
            {
            "id": 437,
            "name": "Lying Close-Grip Bar Curl On High Pulley",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 438,
            "name": "Lying Close-Grip Barbell Triceps Extension Behind The Head",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 439,
            "name": "Lying Close-Grip Barbell Triceps Press To Chin",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 440,
            "name": "Lying Crossover",
            "primaryMuscles": ["abductors"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 441,
            "name": "Lying Dumbbell Tricep Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 442,
            "name": "Lying Face Down Plate Neck Resistance",
            "primaryMuscles": ["neck"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 443,
            "name": "Lying Face Up Plate Neck Resistance",
            "primaryMuscles": ["neck"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 444,
            "name": "Lying Glute",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["abductors"],
            "category": "stretching"
            },
            {
            "id": 445,
            "name": "Lying Hamstring",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves"],
            "category": "stretching"
            },
            {
            "id": 446,
            "name": "Lying High Bench Barbell Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 447,
            "name": "Lying Leg Curls",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 448,
            "name": "Lying Machine Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 449,
            "name": "Lying One-Arm Lateral Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 450,
            "name": "Lying Prone Quadriceps",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 451,
            "name": "Lying Rear Delt Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 452,
            "name": "Lying Supine Dumbbell Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 453,
            "name": "Lying T-Bar Row",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats"],
            "category": "strength"
            },
            {
            "id": 454,
            "name": "Lying Triceps Press",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 455,
            "name": "Machine Bench Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 456,
            "name": "Machine Bicep Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 457,
            "name": "Machine Preacher Curls",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 458,
            "name": "Machine Shoulder (Military) Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 459,
            "name": "Machine Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 460,
            "name": "Medicine Ball Chest Pass",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "plyometrics"
            },
            {
            "id": 461,
            "name": "Medicine Ball Full Twist",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["shoulders"],
            "category": "plyometrics"
            },
            {
            "id": 462,
            "name": "Medicine Ball Scoop Throw",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["abdominals", "hamstrings", "quadriceps"],
            "category": "plyometrics"
            },
            {
            "id": 463,
            "name": "Middle Back Shrug",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 464,
            "name": "Middle Back Stretch",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["abdominals", "lats", "lower back"],
            "category": "stretching"
            },
            {
            "id": 465,
            "name": "Mixed Grip Chin",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats"],
            "category": "strength"
            },
            {
            "id": 466,
            "name": "Monster Walk",
            "primaryMuscles": ["abductors"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 467,
            "name": "Mountain Climbers",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["chest", "hamstrings", "shoulders"],
            "category": "plyometrics"
            },
            {
            "id": 468,
            "name": "Moving Claw Series",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves", "quadriceps"],
            "category": "plyometrics"
            },
            {
            "id": 469,
            "name": "Muscle Snatch",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "glutes",
                "lower back",
                "quadriceps",
                "shoulders",
                "triceps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 470,
            "name": "Muscle Up",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": [
                "abdominals",
                "biceps",
                "forearms",
                "middle back",
                "shoulders",
                "traps",
                "triceps"
            ],
            "category": "strength"
            },
            {
            "id": 471,
            "name": "Narrow Stance Hack Squats",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 472,
            "name": "Narrow Stance Leg Press",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 473,
            "name": "Narrow Stance Squats",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings", "lower back"],
            "category": "strength"
            },
            {
            "id": 474,
            "name": "Natural Glute Ham Raise",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves", "glutes", "lower back"],
            "category": "strength"
            },
            {
            "id": 475,
            "name": "Neck-SMR",
            "primaryMuscles": ["neck"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 476,
            "name": "Neck Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 477,
            "name": "Oblique Crunches",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 478,
            "name": "Oblique Crunches - On The Floor",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 479,
            "name": "Olympic Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "olympic weightlifting"
            },
            {
            "id": 480,
            "name": "On-Your-Back Quad Stretch",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 481,
            "name": "On Your Side Quad Stretch",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 482,
            "name": "One-Arm Dumbbell Row",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats", "shoulders"],
            "category": "strength"
            },
            {
            "id": 483,
            "name": "One-Arm Flat Bench Dumbbell Flye",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 484,
            "name": "One-Arm High-Pulley Cable Side Bends",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 485,
            "name": "One-Arm Incline Lateral Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 486,
            "name": "One-Arm Kettlebell Clean",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["glutes", "lower back", "shoulders", "traps"],
            "category": "strength"
            },
            {
            "id": 487,
            "name": "One-Arm Kettlebell Clean and Jerk",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 488,
            "name": "One-Arm Kettlebell Floor Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 489,
            "name": "One-Arm Kettlebell Jerk",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["calves", "quadriceps", "triceps"],
            "category": "strength"
            },
            {
            "id": 490,
            "name": "One-Arm Kettlebell Military Press To The Side",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 491,
            "name": "One-Arm Kettlebell Para Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 492,
            "name": "One-Arm Kettlebell Push Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["calves", "quadriceps", "triceps"],
            "category": "strength"
            },
            {
            "id": 493,
            "name": "One-Arm Kettlebell Row",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats"],
            "category": "strength"
            },
            {
            "id": 494,
            "name": "One-Arm Kettlebell Snatch",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [
                "calves",
                "glutes",
                "hamstrings",
                "lower back",
                "traps",
                "triceps"
            ],
            "category": "strength"
            },
            {
            "id": 495,
            "name": "One-Arm Kettlebell Split Jerk",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["glutes", "hamstrings", "quadriceps", "triceps"],
            "category": "strength"
            },
            {
            "id": 496,
            "name": "One-Arm Kettlebell Split Snatch",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["hamstrings", "quadriceps"],
            "category": "strength"
            },
            {
            "id": 497,
            "name": "One-Arm Kettlebell Swings",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves", "glutes", "lower back", "shoulders"],
            "category": "strength"
            },
            {
            "id": 498,
            "name": "One-Arm Long Bar Row",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats"],
            "category": "strength"
            },
            {
            "id": 499,
            "name": "One-Arm Medicine Ball Slam",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["lats", "shoulders"],
            "category": "strength"
            },
            {
            "id": 500,
            "name": "One-Arm Open Palm Kettlebell Clean",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "forearms",
                "glutes",
                "lower back",
                "quadriceps",
                "shoulders"
            ],
            "category": "strength"
            },
            {
            "id": 501,
            "name": "One-Arm Overhead Kettlebell Squats",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings", "shoulders"],
            "category": "strength"
            },
            {
            "id": 502,
            "name": "One-Arm Side Deadlift",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "abdominals",
                "calves",
                "glutes",
                "hamstrings",
                "lower back",
                "traps"
            ],
            "category": "strength"
            },
            {
            "id": 503,
            "name": "One-Arm Side Laterals",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 504,
            "name": "One-Legged Cable Kickback",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["hamstrings"],
            "category": "strength"
            },
            {
            "id": 505,
            "name": "One Arm Against Wall",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 506,
            "name": "One Arm Chin-Up",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "forearms", "lats"],
            "category": "strength"
            },
            {
            "id": 507,
            "name": "One Arm Dumbbell Bench Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 508,
            "name": "One Arm Dumbbell Preacher Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 509,
            "name": "One Arm Floor Press",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 510,
            "name": "One Arm Lat Pulldown",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "middle back"],
            "category": "strength"
            },
            {
            "id": 511,
            "name": "One Arm Pronated Dumbbell Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 512,
            "name": "One Arm Supinated Dumbbell Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 513,
            "name": "One Half Locust",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["abdominals", "biceps", "chest"],
            "category": "stretching"
            },
            {
            "id": 514,
            "name": "One Handed Hang",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps"],
            "category": "stretching"
            },
            {
            "id": 515,
            "name": "One Knee To Chest",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["hamstrings", "lower back"],
            "category": "stretching"
            },
            {
            "id": 516,
            "name": "One Leg Barbell Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 517,
            "name": "Open Palm Kettlebell Clean",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["glutes", "lower back", "quadriceps", "shoulders"],
            "category": "strength"
            },
            {
            "id": 518,
            "name": "Otis-Up",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["chest", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 519,
            "name": "Overhead Cable Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 520,
            "name": "Overhead Lat",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["triceps"],
            "category": "stretching"
            },
            {
            "id": 521,
            "name": "Overhead Slam",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": [],
            "category": "plyometrics"
            },
            {
            "id": 522,
            "name": "Overhead Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "abdominals",
                "calves",
                "glutes",
                "hamstrings",
                "lower back",
                "shoulders",
                "triceps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 523,
            "name": "Overhead Stretch",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["chest", "forearms", "lats", "triceps"],
            "category": "stretching"
            },
            {
            "id": 524,
            "name": "Overhead Triceps",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["lats"],
            "category": "stretching"
            },
            {
            "id": 525,
            "name": "Pallof Press",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["chest", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 526,
            "name": "Pallof Press With Rotation",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["chest", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 527,
            "name": "Palms-Down Dumbbell Wrist Curl Over A Bench",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 528,
            "name": "Palms-Down Wrist Curl Over A Bench",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 529,
            "name": "Palms-Up Barbell Wrist Curl Over A Bench",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 530,
            "name": "Palms-Up Dumbbell Wrist Curl Over A Bench",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 531,
            "name": "Parallel Bar Dip",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 532,
            "name": "Pelvic Tilt Into Bridge",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 533,
            "name": "Peroneals-SMR",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 534,
            "name": "Peroneals Stretch",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 535,
            "name": "Physioball Hip Bridge",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["hamstrings"],
            "category": "strength"
            },
            {
            "id": 536,
            "name": "Pin Presses",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [
                "chest",
                "forearms",
                "lats",
                "middle back",
                "shoulders"
            ],
            "category": "powerlifting"
            },
            {
            "id": 537,
            "name": "Piriformis-SMR",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 538,
            "name": "Plank",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 539,
            "name": "Plate Pinch",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 540,
            "name": "Plate Twist",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 541,
            "name": "Platform Hamstring Slides",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["glutes"],
            "category": "strength"
            },
            {
            "id": 542,
            "name": "Plie Dumbbell Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["abdominals", "calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 543,
            "name": "Plyo Kettlebell Pushups",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 544,
            "name": "Plyo Push-up",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "plyometrics"
            },
            {
            "id": 545,
            "name": "Posterior Tibialis Stretch",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 546,
            "name": "Power Clean",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "calves",
                "forearms",
                "glutes",
                "lower back",
                "middle back",
                "quadriceps",
                "shoulders",
                "traps",
                "triceps"
            ],
            "category": "strength"
            },
            {
            "id": 547,
            "name": "Power Clean from Blocks",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["quadriceps"],
            "category": "olympic weightlifting"
            },
            {
            "id": 548,
            "name": "Power Jerk",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "abdominals",
                "calves",
                "glutes",
                "hamstrings",
                "shoulders",
                "triceps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 549,
            "name": "Power Partials",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 550,
            "name": "Power Snatch",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "calves",
                "glutes",
                "lower back",
                "quadriceps",
                "shoulders",
                "traps",
                "triceps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 551,
            "name": "Power Snatch from Blocks",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "calves",
                "forearms",
                "glutes",
                "hamstrings",
                "lower back",
                "shoulders",
                "traps",
                "triceps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 552,
            "name": "Power Stairs",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "adductors",
                "calves",
                "glutes",
                "lower back",
                "quadriceps",
                "shoulders",
                "traps"
            ],
            "category": "strongman"
            },
            {
            "id": 553,
            "name": "Preacher Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 554,
            "name": "Preacher Hammer Dumbbell Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 555,
            "name": "Press Sit-Up",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["chest", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 556,
            "name": "Prone Manual Hamstring",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 557,
            "name": "Prowler Sprint",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "calves",
                "chest",
                "glutes",
                "quadriceps",
                "shoulders"
            ],
            "category": "cardio"
            },
            {
            "id": 558,
            "name": "Pull Through",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["hamstrings", "lower back"],
            "category": "strength"
            },
            {
            "id": 559,
            "name": "Pullups",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "middle back"],
            "category": "strength"
            },
            {
            "id": 560,
            "name": "Push-Up Wide",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["abdominals", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 561,
            "name": "Push-Ups - Close Triceps Position",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 562,
            "name": "Push-Ups With Feet Elevated",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 563,
            "name": "Push-Ups With Feet On An Exercise Ball",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 564,
            "name": "Push Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["quadriceps", "triceps"],
            "category": "olympic weightlifting"
            },
            {
            "id": 565,
            "name": "Push Press - Behind the Neck",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["calves", "quadriceps", "triceps"],
            "category": "olympic weightlifting"
            },
            {
            "id": 566,
            "name": "Push Up to Side Plank",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["abdominals", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 567,
            "name": "Pushups",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 568,
            "name": "Pushups (Close and Wide Hand Positions)",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 569,
            "name": "Pyramid",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": ["shoulders"],
            "category": "stretching"
            },
            {
            "id": 570,
            "name": "Quad Stretch",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 571,
            "name": "Quadriceps-SMR",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 572,
            "name": "Quick Leap",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "hamstrings"],
            "category": "plyometrics"
            },
            {
            "id": 573,
            "name": "Rack Delivery",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["forearms", "traps"],
            "category": "olympic weightlifting"
            },
            {
            "id": 574,
            "name": "Rack Pull with Bands",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": [
                "forearms",
                "glutes",
                "hamstrings",
                "quadriceps",
                "traps"
            ],
            "category": "powerlifting"
            },
            {
            "id": 575,
            "name": "Rack Pulls",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": ["forearms", "glutes", "hamstrings", "traps"],
            "category": "powerlifting"
            },
            {
            "id": 576,
            "name": "Rear Leg Raises",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 577,
            "name": "Recumbent Bike",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "cardio"
            },
            {
            "id": 578,
            "name": "Return Push from Stance",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["chest", "triceps"],
            "category": "plyometrics"
            },
            {
            "id": 579,
            "name": "Reverse Band Bench Press",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [
                "chest",
                "forearms",
                "lats",
                "middle back",
                "shoulders"
            ],
            "category": "powerlifting"
            },
            {
            "id": 580,
            "name": "Reverse Band Box Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "abductors",
                "adductors",
                "calves",
                "forearms",
                "glutes",
                "hamstrings",
                "lower back"
            ],
            "category": "powerlifting"
            },
            {
            "id": 581,
            "name": "Reverse Band Deadlift",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": [
                "abductors",
                "adductors",
                "calves",
                "glutes",
                "hamstrings",
                "quadriceps"
            ],
            "category": "powerlifting"
            },
            {
            "id": 582,
            "name": "Reverse Band Power Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "adductors",
                "calves",
                "glutes",
                "hamstrings",
                "lower back"
            ],
            "category": "powerlifting"
            },
            {
            "id": 583,
            "name": "Reverse Band Sumo Deadlift",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "abductors",
                "adductors",
                "calves",
                "forearms",
                "glutes",
                "lower back",
                "quadriceps",
                "traps"
            ],
            "category": "powerlifting"
            },
            {
            "id": 584,
            "name": "Reverse Barbell Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 585,
            "name": "Reverse Barbell Preacher Curls",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 586,
            "name": "Reverse Cable Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 587,
            "name": "Reverse Crunch",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 588,
            "name": "Reverse Flyes",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 589,
            "name": "Reverse Flyes With External Rotation",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 590,
            "name": "Reverse Grip Bent-Over Rows",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats", "shoulders"],
            "category": "strength"
            },
            {
            "id": 591,
            "name": "Reverse Grip Triceps Pushdown",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 592,
            "name": "Reverse Hyperextension",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves", "glutes"],
            "category": "strength"
            },
            {
            "id": 593,
            "name": "Reverse Machine Flyes",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 594,
            "name": "Reverse Plate Curls",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 595,
            "name": "Reverse Triceps Bench Press",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 596,
            "name": "Rhomboids-SMR",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["traps"],
            "category": "stretching"
            },
            {
            "id": 597,
            "name": "Rickshaw Carry",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [
                "abdominals",
                "calves",
                "glutes",
                "hamstrings",
                "lower back",
                "quadriceps",
                "traps"
            ],
            "category": "strongman"
            },
            {
            "id": 598,
            "name": "Rickshaw Deadlift",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "forearms",
                "glutes",
                "hamstrings",
                "lower back",
                "traps"
            ],
            "category": "strongman"
            },
            {
            "id": 599,
            "name": "Ring Dips",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 600,
            "name": "Rocket Jump",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "hamstrings"],
            "category": "plyometrics"
            },
            {
            "id": 601,
            "name": "Rocking Standing Calf Raise",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 602,
            "name": "Rocky Pull-Ups/Pulldowns",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "middle back", "shoulders"],
            "category": "strength"
            },
            {
            "id": 603,
            "name": "Romanian Deadlift",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves", "glutes", "lower back"],
            "category": "strength"
            },
            {
            "id": 604,
            "name": "Romanian Deadlift from Deficit",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["forearms", "glutes", "lower back", "traps"],
            "category": "olympic weightlifting"
            },
            {
            "id": 605,
            "name": "Rope Climb",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "forearms", "middle back", "shoulders"],
            "category": "strength"
            },
            {
            "id": 606,
            "name": "Rope Crunch",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 607,
            "name": "Rope Jumping",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "hamstrings"],
            "category": "cardio"
            },
            {
            "id": 608,
            "name": "Rope Straight-Arm Pulldown",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 609,
            "name": "Round The World Shoulder Stretch",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["biceps", "chest"],
            "category": "stretching"
            },
            {
            "id": 610,
            "name": "Rowing, Stationary",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "biceps",
                "calves",
                "glutes",
                "hamstrings",
                "lower back",
                "middle back"
            ],
            "category": "cardio"
            },
            {
            "id": 611,
            "name": "Runner's Stretch",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves"],
            "category": "stretching"
            },
            {
            "id": 612,
            "name": "Running, Treadmill",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "cardio"
            },
            {
            "id": 613,
            "name": "Russian Twist",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["lower back"],
            "category": "strength"
            },
            {
            "id": 614,
            "name": "Sandbag Load",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "abdominals",
                "biceps",
                "calves",
                "forearms",
                "glutes",
                "hamstrings",
                "lower back",
                "middle back",
                "shoulders",
                "traps"
            ],
            "category": "strongman"
            },
            {
            "id": 615,
            "name": "Scapular Pull-Up",
            "primaryMuscles": ["traps"],
            "secondaryMuscles": ["lats", "middle back"],
            "category": "strength"
            },
            {
            "id": 616,
            "name": "Scissor Kick",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 617,
            "name": "Scissors Jump",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["glutes", "hamstrings"],
            "category": "plyometrics"
            },
            {
            "id": 618,
            "name": "Seated Band Hamstring Curl",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 619,
            "name": "Seated Barbell Military Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 620,
            "name": "Seated Barbell Twist",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 621,
            "name": "Seated Bent-Over One-Arm Dumbbell Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 622,
            "name": "Seated Bent-Over Rear Delt Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 623,
            "name": "Seated Bent-Over Two-Arm Dumbbell Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 624,
            "name": "Seated Biceps",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "stretching"
            },
            {
            "id": 625,
            "name": "Seated Cable Rows",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats", "shoulders"],
            "category": "strength"
            },
            {
            "id": 626,
            "name": "Seated Cable Shoulder Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 627,
            "name": "Seated Calf Raise",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 628,
            "name": "Seated Calf Stretch",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": ["hamstrings", "lower back"],
            "category": "stretching"
            },
            {
            "id": 629,
            "name": "Seated Close-Grip Concentration Barbell Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 630,
            "name": "Seated Dumbbell Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 631,
            "name": "Seated Dumbbell Inner Biceps Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 632,
            "name": "Seated Dumbbell Palms-Down Wrist Curl",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 633,
            "name": "Seated Dumbbell Palms-Up Wrist Curl",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 634,
            "name": "Seated Dumbbell Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 635,
            "name": "Seated Flat Bench Leg Pull-In",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 636,
            "name": "Seated Floor Hamstring Stretch",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves"],
            "category": "stretching"
            },
            {
            "id": 637,
            "name": "Seated Front Deltoid",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["chest"],
            "category": "stretching"
            },
            {
            "id": 638,
            "name": "Seated Glute",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["adductors"],
            "category": "stretching"
            },
            {
            "id": 639,
            "name": "Seated Good Mornings",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": ["glutes"],
            "category": "powerlifting"
            },
            {
            "id": 640,
            "name": "Seated Hamstring",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves"],
            "category": "stretching"
            },
            {
            "id": 641,
            "name": "Seated Hamstring and Calf Stretch",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves"],
            "category": "stretching"
            },
            {
            "id": 642,
            "name": "Seated Head Harness Neck Resistance",
            "primaryMuscles": ["neck"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 643,
            "name": "Seated Leg Curl",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 644,
            "name": "Seated Leg Tucks",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 645,
            "name": "Seated One-Arm Dumbbell Palms-Down Wrist Curl",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 646,
            "name": "Seated One-Arm Dumbbell Palms-Up Wrist Curl",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 647,
            "name": "Seated One-arm Cable Pulley Rows",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats", "traps"],
            "category": "strength"
            },
            {
            "id": 648,
            "name": "Seated Overhead Stretch",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 649,
            "name": "Seated Palm-Up Barbell Wrist Curl",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 650,
            "name": "Seated Palms-Down Barbell Wrist Curl",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 651,
            "name": "Seated Side Lateral Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 652,
            "name": "Seated Triceps Press",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 653,
            "name": "Seated Two-Arm Palms-Up Low-Pulley Wrist Curl",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 654,
            "name": "See-Saw Press (Alternating Side Press)",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["abdominals", "triceps"],
            "category": "strength"
            },
            {
            "id": 655,
            "name": "Shotgun Row",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "middle back"],
            "category": "strength"
            },
            {
            "id": 656,
            "name": "Shoulder Circles",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["traps"],
            "category": "stretching"
            },
            {
            "id": 657,
            "name": "Shoulder Press - With Bands",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 658,
            "name": "Shoulder Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["lats"],
            "category": "stretching"
            },
            {
            "id": 659,
            "name": "Shoulder Stretch",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 660,
            "name": "Side-Lying Floor Stretch",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 661,
            "name": "Side Bridge",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["shoulders"],
            "category": "strength"
            },
            {
            "id": 662,
            "name": "Side Hop-Sprint",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["abductors", "adductors", "calves", "hamstrings"],
            "category": "plyometrics"
            },
            {
            "id": 663,
            "name": "Side Jackknife",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 664,
            "name": "Side Lateral Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 665,
            "name": "Side Laterals to Front Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["traps"],
            "category": "strength"
            },
            {
            "id": 666,
            "name": "Side Leg Raises",
            "primaryMuscles": ["adductors"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 667,
            "name": "Side Lying Groin Stretch",
            "primaryMuscles": ["adductors"],
            "secondaryMuscles": ["hamstrings"],
            "category": "stretching"
            },
            {
            "id": 668,
            "name": "Side Neck Stretch",
            "primaryMuscles": ["neck"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 669,
            "name": "Side Standing Long Jump",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "plyometrics"
            },
            {
            "id": 670,
            "name": "Side To Side Chins",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "forearms", "middle back", "shoulders"],
            "category": "strength"
            },
            {
            "id": 671,
            "name": "Side Wrist Pull",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["forearms", "lats"],
            "category": "stretching"
            },
            {
            "id": 672,
            "name": "Side to Side Box Shuffle",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["abductors", "adductors", "calves", "hamstrings"],
            "category": "plyometrics"
            },
            {
            "id": 673,
            "name": "Single-Arm Cable Crossover",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 674,
            "name": "Single-Arm Linear Jammer",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["chest", "triceps"],
            "category": "strength"
            },
            {
            "id": 675,
            "name": "Single-Arm Push-Up",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 676,
            "name": "Single-Cone Sprint Drill",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "plyometrics"
            },
            {
            "id": 677,
            "name": "Single-Leg High Box Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 678,
            "name": "Single-Leg Hop Progression",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["abductors", "adductors", "calves", "hamstrings"],
            "category": "plyometrics"
            },
            {
            "id": 679,
            "name": "Single-Leg Lateral Hop",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["abductors", "adductors", "calves", "hamstrings"],
            "category": "plyometrics"
            },
            {
            "id": 680,
            "name": "Single-Leg Leg Extension",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 681,
            "name": "Single-Leg Stride Jump",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["abductors", "adductors", "calves", "hamstrings"],
            "category": "plyometrics"
            },
            {
            "id": 682,
            "name": "Single Dumbbell Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["forearms", "traps"],
            "category": "strength"
            },
            {
            "id": 683,
            "name": "Single Leg Butt Kick",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "hamstrings"],
            "category": "plyometrics"
            },
            {
            "id": 684,
            "name": "Single Leg Glute Bridge",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["hamstrings"],
            "category": "strength"
            },
            {
            "id": 685,
            "name": "Single Leg Push-off",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "hamstrings"],
            "category": "plyometrics"
            },
            {
            "id": 686,
            "name": "Sit-Up",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 687,
            "name": "Sit Squats",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["abductors", "glutes", "hamstrings"],
            "category": "stretching"
            },
            {
            "id": 688,
            "name": "Skating",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "abductors",
                "adductors",
                "calves",
                "glutes",
                "hamstrings"
            ],
            "category": "cardio"
            },
            {
            "id": 689,
            "name": "Sled Drag - Harness",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strongman"
            },
            {
            "id": 690,
            "name": "Sled Overhead Backward Walk",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["calves", "middle back", "quadriceps"],
            "category": "strength"
            },
            {
            "id": 691,
            "name": "Sled Overhead Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 692,
            "name": "Sled Push",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "calves",
                "chest",
                "glutes",
                "hamstrings",
                "triceps"
            ],
            "category": "strongman"
            },
            {
            "id": 693,
            "name": "Sled Reverse Flye",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 694,
            "name": "Sled Row",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats"],
            "category": "strength"
            },
            {
            "id": 695,
            "name": "Sledgehammer Swings",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [
                "calves",
                "forearms",
                "lats",
                "middle back",
                "shoulders"
            ],
            "category": "plyometrics"
            },
            {
            "id": 696,
            "name": "Smith Incline Shoulder Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["chest"],
            "category": "strength"
            },
            {
            "id": 697,
            "name": "Smith Machine Behind the Back Shrug",
            "primaryMuscles": ["traps"],
            "secondaryMuscles": ["shoulders"],
            "category": "strength"
            },
            {
            "id": 698,
            "name": "Smith Machine Bench Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 699,
            "name": "Smith Machine Bent Over Row",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats", "shoulders"],
            "category": "strength"
            },
            {
            "id": 700,
            "name": "Smith Machine Calf Raise",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 701,
            "name": "Smith Machine Close-Grip Bench Press",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 702,
            "name": "Smith Machine Decline Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 703,
            "name": "Smith Machine Hang Power Clean",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "glutes",
                "lower back",
                "quadriceps",
                "shoulders",
                "traps"
            ],
            "category": "strength"
            },
            {
            "id": 704,
            "name": "Smith Machine Hip Raise",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 705,
            "name": "Smith Machine Incline Bench Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 706,
            "name": "Smith Machine Leg Press",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 707,
            "name": "Smith Machine One-Arm Upright Row",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["biceps", "traps"],
            "category": "strength"
            },
            {
            "id": 708,
            "name": "Smith Machine Overhead Shoulder Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 709,
            "name": "Smith Machine Pistol Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 710,
            "name": "Smith Machine Reverse Calf Raises",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 711,
            "name": "Smith Machine Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings", "lower back"],
            "category": "strength"
            },
            {
            "id": 712,
            "name": "Smith Machine Stiff-Legged Deadlift",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["glutes", "lower back"],
            "category": "strength"
            },
            {
            "id": 713,
            "name": "Smith Machine Upright Row",
            "primaryMuscles": ["traps"],
            "secondaryMuscles": ["biceps", "middle back", "shoulders"],
            "category": "strength"
            },
            {
            "id": 714,
            "name": "Smith Single-Leg Split Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 715,
            "name": "Snatch",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "biceps",
                "glutes",
                "hamstrings",
                "lower back",
                "shoulders",
                "traps",
                "triceps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 716,
            "name": "Snatch Balance",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "calves",
                "glutes",
                "hamstrings",
                "shoulders",
                "triceps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 717,
            "name": "Snatch Deadlift",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "forearms",
                "glutes",
                "hamstrings",
                "lower back",
                "quadriceps",
                "traps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 718,
            "name": "Snatch Pull",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "calves",
                "glutes",
                "lower back",
                "quadriceps",
                "traps"
            ],
            "category": "strength"
            },
            {
            "id": 719,
            "name": "Snatch Shrug",
            "primaryMuscles": ["traps"],
            "secondaryMuscles": ["forearms", "shoulders"],
            "category": "olympic weightlifting"
            },
            {
            "id": 720,
            "name": "Snatch from Blocks",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "calves",
                "forearms",
                "glutes",
                "hamstrings",
                "lower back",
                "shoulders",
                "traps",
                "triceps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 721,
            "name": "Speed Band Overhead Triceps",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 722,
            "name": "Speed Box Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "powerlifting"
            },
            {
            "id": 723,
            "name": "Speed Squats",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings", "lower back"],
            "category": "strength"
            },
            {
            "id": 724,
            "name": "Spell Caster",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["glutes", "shoulders"],
            "category": "strength"
            },
            {
            "id": 725,
            "name": "Spider Crawl",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["chest", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 726,
            "name": "Spider Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 727,
            "name": "Spinal Stretch",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["lats", "lower back", "neck", "traps"],
            "category": "stretching"
            },
            {
            "id": 728,
            "name": "Split Clean",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "calves",
                "forearms",
                "glutes",
                "hamstrings",
                "lower back",
                "shoulders",
                "traps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 729,
            "name": "Split Jerk",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["glutes", "hamstrings", "shoulders", "triceps"],
            "category": "olympic weightlifting"
            },
            {
            "id": 730,
            "name": "Split Jump",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "plyometrics"
            },
            {
            "id": 731,
            "name": "Split Snatch",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "calves",
                "forearms",
                "glutes",
                "hamstrings",
                "lower back",
                "quadriceps",
                "shoulders",
                "traps",
                "triceps"
            ],
            "category": "olympic weightlifting"
            },
            {
            "id": 732,
            "name": "Split Squat with Dumbbells",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 733,
            "name": "Split Squats",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves", "glutes", "quadriceps"],
            "category": "stretching"
            },
            {
            "id": 734,
            "name": "Squat Jerk",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "calves",
                "glutes",
                "hamstrings",
                "shoulders",
                "triceps"
            ],
            "category": "strength"
            },
            {
            "id": 735,
            "name": "Squat with Bands",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "adductors",
                "calves",
                "glutes",
                "hamstrings",
                "lower back"
            ],
            "category": "powerlifting"
            },
            {
            "id": 736,
            "name": "Squat with Chains",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "adductors",
                "calves",
                "glutes",
                "hamstrings",
                "lower back"
            ],
            "category": "powerlifting"
            },
            {
            "id": 737,
            "name": "Squat with Plate Movers",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "abductors",
                "adductors",
                "calves",
                "glutes",
                "hamstrings"
            ],
            "category": "strength"
            },
            {
            "id": 738,
            "name": "Squats - With Bands",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings", "lower back"],
            "category": "strength"
            },
            {
            "id": 739,
            "name": "Stairmaster",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "cardio"
            },
            {
            "id": 740,
            "name": "Standing Alternating Dumbbell Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 741,
            "name": "Standing Barbell Calf Raise",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 742,
            "name": "Standing Barbell Press Behind Neck",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 743,
            "name": "Standing Bent-Over One-Arm Dumbbell Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["shoulders"],
            "category": "strength"
            },
            {
            "id": 744,
            "name": "Standing Bent-Over Two-Arm Dumbbell Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 745,
            "name": "Standing Biceps Cable Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 746,
            "name": "Standing Biceps Stretch",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "stretching"
            },
            {
            "id": 747,
            "name": "Standing Bradford Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 748,
            "name": "Standing Cable Chest Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 749,
            "name": "Standing Cable Lift",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["shoulders"],
            "category": "strength"
            },
            {
            "id": 750,
            "name": "Standing Cable Wood Chop",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["shoulders"],
            "category": "strength"
            },
            {
            "id": 751,
            "name": "Standing Calf Raises",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 752,
            "name": "Standing Concentration Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 753,
            "name": "Standing Dumbbell Calf Raise",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 754,
            "name": "Standing Dumbbell Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 755,
            "name": "Standing Dumbbell Reverse Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 756,
            "name": "Standing Dumbbell Straight-Arm Front Delt Raise Above Head",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 757,
            "name": "Standing Dumbbell Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 758,
            "name": "Standing Dumbbell Upright Row",
            "primaryMuscles": ["traps"],
            "secondaryMuscles": ["biceps", "shoulders"],
            "category": "strength"
            },
            {
            "id": 759,
            "name": "Standing Elevated Quad Stretch",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 760,
            "name": "Standing Front Barbell Raise Over Head",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 761,
            "name": "Standing Gastrocnemius Calf Stretch",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": ["hamstrings"],
            "category": "stretching"
            },
            {
            "id": 762,
            "name": "Standing Hamstring and Calf Stretch",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 763,
            "name": "Standing Hip Circles",
            "primaryMuscles": ["abductors"],
            "secondaryMuscles": ["adductors"],
            "category": "stretching"
            },
            {
            "id": 764,
            "name": "Standing Hip Flexors",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 765,
            "name": "Standing Inner-Biceps Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 766,
            "name": "Standing Lateral Stretch",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 767,
            "name": "Standing Leg Curl",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 768,
            "name": "Standing Long Jump",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "plyometrics"
            },
            {
            "id": 769,
            "name": "Standing Low-Pulley Deltoid Raise",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 770,
            "name": "Standing Low-Pulley One-Arm Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 771,
            "name": "Standing Military Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 772,
            "name": "Standing Olympic Plate Hand Squeeze",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": ["biceps"],
            "category": "strength"
            },
            {
            "id": 773,
            "name": "Standing One-Arm Cable Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 774,
            "name": "Standing One-Arm Dumbbell Curl Over Incline Bench",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 775,
            "name": "Standing One-Arm Dumbbell Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 776,
            "name": "Standing Overhead Barbell Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["shoulders"],
            "category": "strength"
            },
            {
            "id": 777,
            "name": "Standing Palm-In One-Arm Dumbbell Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 778,
            "name": "Standing Palms-In Dumbbell Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 779,
            "name": "Standing Palms-Up Barbell Behind The Back Wrist Curl",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 780,
            "name": "Standing Pelvic Tilt",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": ["glutes"],
            "category": "stretching"
            },
            {
            "id": 781,
            "name": "Standing Rope Crunch",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 782,
            "name": "Standing Soleus And Achilles Stretch",
            "primaryMuscles": ["calves"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 783,
            "name": "Standing Toe Touches",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves"],
            "category": "stretching"
            },
            {
            "id": 784,
            "name": "Standing Towel Triceps Extension",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 785,
            "name": "Standing Two-Arm Overhead Throw",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["chest", "lats"],
            "category": "plyometrics"
            },
            {
            "id": 786,
            "name": "Star Jump",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings", "shoulders"],
            "category": "plyometrics"
            },
            {
            "id": 787,
            "name": "Step-up with Knee Raise",
            "primaryMuscles": ["glutes"],
            "secondaryMuscles": ["hamstrings", "quadriceps"],
            "category": "strength"
            },
            {
            "id": 788,
            "name": "Step Mill",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "cardio"
            },
            {
            "id": 789,
            "name": "Stiff-Legged Barbell Deadlift",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["glutes", "lower back"],
            "category": "strength"
            },
            {
            "id": 790,
            "name": "Stiff-Legged Dumbbell Deadlift",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["glutes", "lower back"],
            "category": "strength"
            },
            {
            "id": 791,
            "name": "Stiff Leg Barbell Good Morning",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": ["glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 792,
            "name": "Stomach Vacuum",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 793,
            "name": "Straight-Arm Dumbbell Pullover",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["lats", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 794,
            "name": "Straight-Arm Pulldown",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 795,
            "name": "Straight Bar Bench Mid Rows",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats"],
            "category": "strength"
            },
            {
            "id": 796,
            "name": "Straight Raises on Incline Bench",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["traps"],
            "category": "strength"
            },
            {
            "id": 797,
            "name": "Stride Jump Crossover",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["abductors", "adductors", "calves", "hamstrings"],
            "category": "plyometrics"
            },
            {
            "id": 798,
            "name": "Sumo Deadlift",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "adductors",
                "forearms",
                "glutes",
                "lower back",
                "middle back",
                "quadriceps",
                "traps"
            ],
            "category": "powerlifting"
            },
            {
            "id": 799,
            "name": "Sumo Deadlift with Bands",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "adductors",
                "forearms",
                "glutes",
                "lower back",
                "middle back",
                "quadriceps",
                "traps"
            ],
            "category": "powerlifting"
            },
            {
            "id": 800,
            "name": "Sumo Deadlift with Chains",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": [
                "abductors",
                "adductors",
                "forearms",
                "glutes",
                "lower back",
                "middle back",
                "quadriceps",
                "traps"
            ],
            "category": "powerlifting"
            },
            {
            "id": 801,
            "name": "Superman",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": ["glutes", "hamstrings"],
            "category": "stretching"
            },
            {
            "id": 802,
            "name": "Supine Chest Throw",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "plyometrics"
            },
            {
            "id": 803,
            "name": "Supine One-Arm Overhead Throw",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["chest", "lats", "shoulders"],
            "category": "plyometrics"
            },
            {
            "id": 804,
            "name": "Supine Two-Arm Overhead Throw",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["chest", "lats", "shoulders"],
            "category": "plyometrics"
            },
            {
            "id": 805,
            "name": "Suspended Fallout",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": ["chest", "lower back", "shoulders"],
            "category": "strength"
            },
            {
            "id": 806,
            "name": "Suspended Push-Up",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 807,
            "name": "Suspended Reverse Crunch",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 808,
            "name": "Suspended Row",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats"],
            "category": "strength"
            },
            {
            "id": 809,
            "name": "Suspended Split Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "abductors",
                "adductors",
                "calves",
                "glutes",
                "hamstrings"
            ],
            "category": "strength"
            },
            {
            "id": 810,
            "name": "Svend Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["forearms", "shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 811,
            "name": "T-Bar Row with Handle",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats"],
            "category": "strength"
            },
            {
            "id": 812,
            "name": "Tate Press",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 813,
            "name": "The Straddle",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["adductors", "calves"],
            "category": "stretching"
            },
            {
            "id": 814,
            "name": "Thigh Abductor",
            "primaryMuscles": ["abductors"],
            "secondaryMuscles": ["glutes"],
            "category": "strength"
            },
            {
            "id": 815,
            "name": "Thigh Adductor",
            "primaryMuscles": ["adductors"],
            "secondaryMuscles": ["glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 816,
            "name": "Tire Flip",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "calves",
                "chest",
                "forearms",
                "glutes",
                "hamstrings",
                "lower back",
                "shoulders",
                "traps",
                "triceps"
            ],
            "category": "strongman"
            },
            {
            "id": 817,
            "name": "Toe Touchers",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 818,
            "name": "Torso Rotation",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 819,
            "name": "Trail Running/Walking",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "cardio"
            },
            {
            "id": 820,
            "name": "Trap Bar Deadlift",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 821,
            "name": "Tricep Dumbbell Kickback",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 822,
            "name": "Tricep Side Stretch",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["shoulders"],
            "category": "stretching"
            },
            {
            "id": 823,
            "name": "Triceps Overhead Extension with Rope",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 824,
            "name": "Triceps Pushdown",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 825,
            "name": "Triceps Pushdown - Rope Attachment",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 826,
            "name": "Triceps Pushdown - V-Bar Attachment",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 827,
            "name": "Triceps Stretch",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["lats"],
            "category": "stretching"
            },
            {
            "id": 828,
            "name": "Tuck Crunch",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 829,
            "name": "Two-Arm Dumbbell Preacher Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 830,
            "name": "Two-Arm Kettlebell Clean",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": [
                "calves",
                "glutes",
                "hamstrings",
                "lower back",
                "traps"
            ],
            "category": "strength"
            },
            {
            "id": 831,
            "name": "Two-Arm Kettlebell Jerk",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["calves", "quadriceps", "triceps"],
            "category": "strength"
            },
            {
            "id": 832,
            "name": "Two-Arm Kettlebell Military Press",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["triceps"],
            "category": "strength"
            },
            {
            "id": 833,
            "name": "Two-Arm Kettlebell Row",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["biceps", "lats"],
            "category": "strength"
            },
            {
            "id": 834,
            "name": "Underhand Cable Pulldowns",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "middle back", "shoulders"],
            "category": "strength"
            },
            {
            "id": 835,
            "name": "Upper Back-Leg Grab",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["lower back", "middle back"],
            "category": "stretching"
            },
            {
            "id": 836,
            "name": "Upper Back Stretch",
            "primaryMuscles": ["middle back"],
            "secondaryMuscles": ["middle back"],
            "category": "stretching"
            },
            {
            "id": 837,
            "name": "Upright Barbell Row",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["traps"],
            "category": "strength"
            },
            {
            "id": 838,
            "name": "Upright Cable Row",
            "primaryMuscles": ["traps"],
            "secondaryMuscles": ["shoulders"],
            "category": "strength"
            },
            {
            "id": 839,
            "name": "Upright Row - With Bands",
            "primaryMuscles": ["traps"],
            "secondaryMuscles": ["shoulders"],
            "category": "strength"
            },
            {
            "id": 840,
            "name": "Upward Stretch",
            "primaryMuscles": ["shoulders"],
            "secondaryMuscles": ["chest", "lats"],
            "category": "stretching"
            },
            {
            "id": 841,
            "name": "V-Bar Pulldown",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "middle back", "shoulders"],
            "category": "strength"
            },
            {
            "id": 842,
            "name": "V-Bar Pullup",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "middle back", "shoulders"],
            "category": "strength"
            },
            {
            "id": 843,
            "name": "Vertical Swing",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["glutes", "quadriceps", "shoulders"],
            "category": "plyometrics"
            },
            {
            "id": 844,
            "name": "Walking, Treadmill",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "cardio"
            },
            {
            "id": 845,
            "name": "Weighted Ball Hyperextension",
            "primaryMuscles": ["lower back"],
            "secondaryMuscles": ["glutes", "hamstrings", "middle back"],
            "category": "strength"
            },
            {
            "id": 846,
            "name": "Weighted Ball Side Bend",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 847,
            "name": "Weighted Bench Dip",
            "primaryMuscles": ["triceps"],
            "secondaryMuscles": ["chest", "shoulders"],
            "category": "strength"
            },
            {
            "id": 848,
            "name": "Weighted Crunches",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 849,
            "name": "Weighted Jump Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings", "lower back"],
            "category": "strength"
            },
            {
            "id": 850,
            "name": "Weighted Pull Ups",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "middle back"],
            "category": "strength"
            },
            {
            "id": 851,
            "name": "Weighted Sissy Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 852,
            "name": "Weighted Sit-Ups - With Bands",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 853,
            "name": "Weighted Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 854,
            "name": "Wide-Grip Barbell Bench Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 855,
            "name": "Wide-Grip Decline Barbell Bench Press",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 856,
            "name": "Wide-Grip Decline Barbell Pullover",
            "primaryMuscles": ["chest"],
            "secondaryMuscles": ["shoulders", "triceps"],
            "category": "strength"
            },
            {
            "id": 857,
            "name": "Wide-Grip Lat Pulldown",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "middle back", "shoulders"],
            "category": "strength"
            },
            {
            "id": 858,
            "name": "Wide-Grip Pulldown Behind The Neck",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "middle back", "shoulders"],
            "category": "strength"
            },
            {
            "id": 859,
            "name": "Wide-Grip Rear Pull-Up",
            "primaryMuscles": ["lats"],
            "secondaryMuscles": ["biceps", "middle back", "shoulders"],
            "category": "strength"
            },
            {
            "id": 860,
            "name": "Wide-Grip Standing Barbell Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 861,
            "name": "Wide Stance Barbell Squat",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings", "lower back"],
            "category": "strength"
            },
            {
            "id": 862,
            "name": "Wide Stance Stiff Legs",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["adductors", "glutes", "lower back"],
            "category": "olympic weightlifting"
            },
            {
            "id": 863,
            "name": "Wind Sprints",
            "primaryMuscles": ["abdominals"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 864,
            "name": "Windmills",
            "primaryMuscles": ["abductors"],
            "secondaryMuscles": ["glutes", "hamstrings", "lower back"],
            "category": "stretching"
            },
            {
            "id": 865,
            "name": "World's Greatest Stretch",
            "primaryMuscles": ["hamstrings"],
            "secondaryMuscles": ["calves", "glutes", "quadriceps"],
            "category": "stretching"
            },
            {
            "id": 866,
            "name": "Wrist Circles",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "stretching"
            },
            {
            "id": 867,
            "name": "Wrist Roller",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": ["shoulders"],
            "category": "strength"
            },
            {
            "id": 868,
            "name": "Wrist Rotations with Straight Bar",
            "primaryMuscles": ["forearms"],
            "secondaryMuscles": [],
            "category": "strength"
            },
            {
            "id": 869,
            "name": "Yoke Walk",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": [
                "abdominals",
                "abductors",
                "adductors",
                "calves",
                "glutes",
                "hamstrings",
                "lower back"
            ],
            "category": "strongman"
            },
            {
            "id": 870,
            "name": "Zercher Squats",
            "primaryMuscles": ["quadriceps"],
            "secondaryMuscles": ["calves", "glutes", "hamstrings"],
            "category": "strength"
            },
            {
            "id": 871,
            "name": "Zottman Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            },
            {
            "id": 872,
            "name": "Zottman Preacher Curl",
            "primaryMuscles": ["biceps"],
            "secondaryMuscles": ["forearms"],
            "category": "strength"
            }
        ],
        multiinsert=False
    )

def downgrade():
    op.drop_table('exercises')
