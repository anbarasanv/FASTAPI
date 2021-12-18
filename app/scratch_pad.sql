-- Getting the vote count
select posts.*,
    count(votes.post_id) as votes
from posts
    left join votes on posts.id = votes.post_id
group by posts.id
order by posts.id;