SELECT users.first_name as friend_first_name, users.last_name as friend_last_name
FROM users 
JOIN friendships ON users.id = friendships.users.id;