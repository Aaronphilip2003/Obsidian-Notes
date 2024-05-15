

### 1. Points System

**Data Structure:**

- **UserPoints Table:** Store user IDs, activity IDs, points earned per activity, and total points.

```python
class UserPoints:
    user_id: int
    activity_id: int
    points_earned: int
    total_points: int
```

**Business Logic:**

- Award points after completing activities or assessments.
- Sum points for activities to update the total points.

### 2. Badges

**Data Structure:**

- **Badges Table:** Store badge IDs, names, criteria (like points threshold or specific achievements), and descriptions.
- **UserBadges Table:** Store records of badges awarded to users.

```python
class Badge:
    badge_id: int
    name: str
    criteria: str
    description: str

class UserBadge:
    user_id: int
    badge_id: int
```

**Business Logic:**

- Check user achievements against badge criteria (e.g., reaching a points threshold).
- Award badges when criteria are met.

### 3. Levels

**Data Structure:**

- **Levels Table:** Define levels based on points or achievements, with each level having a minimum points requirement.

```python
class Level:
    level_id: int
    level_number: int
    min_points: int
    description: str
```

**Business Logic:**

- Increase user level based on total points or specific achievements.
- Notify users upon reaching a new level.

### 4. Challenges and Quests

**Data Structure:**

- **Challenges Table:** Store challenge IDs, descriptions, points or badges awarded upon completion, and completion criteria.

```python
class Challenge:
    challenge_id: int
    description: str
    reward_points: int
    reward_badge_id: int  # Optional, can be None
    criteria: str  # Could be specific activities or achievements
```

**Business Logic:**

- Allow users to enroll in challenges.
- Track user progress against challenge criteria.
- Award points or badges upon challenge completion.

### 5. Leaderboard

**Data Structure:**

- Utilize the `UserPoints` table to create a dynamic leaderboard.

```python
# Leaderboard can be a view or query rather than a separate table
```

**Business Logic:**

- Calculate total points for each user.
- Sort users by total points in descending order for the leaderboard.
- Optionally, filter leaderboard by time (e.g., weekly, monthly).