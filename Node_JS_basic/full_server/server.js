import express from 'express';
import router from './routes/index.js';

const app = express();
const PORT = 1245;

// Use the routes defined in routes/index.js
app.use('/', router);

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});

export default app;
