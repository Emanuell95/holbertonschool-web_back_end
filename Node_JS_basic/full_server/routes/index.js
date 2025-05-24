import { Router } from 'express';
import AppController from '../controllers/AppController.js';
import StudentsController from '../controllers/StudentsController.js';

const router = Router();

// Link route / to AppController
router.get('/', AppController.getHomepage);

// Link routes /students and /students/:major to StudentsController
router.get('/students', StudentsController.getAllStudents);
router.get('/students/:major', StudentsController.getAllStudentsByMajor);

export default router;
