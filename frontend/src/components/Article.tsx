import React from 'react';

interface ArticleProps {
  id: number;
  title: string;
  content: string;
  author: string;
  publishedAt: string;
}

const Article: React.FC<ArticleProps> = ({ id, title, content, author, publishedAt }) => {
  return (
    <div className="Article">
      <h2>{title}</h2>
      <p>{content}</p>
      <small>By {author} on {new Date(publishedAt).toLocaleDateString()}</small>
    </div>
  );
}

export default Article;
