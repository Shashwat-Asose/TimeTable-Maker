# 📅 **Teacher Timetable Generator**
![Logo](./logo.png)
An intelligent and dynamic Python-based scheduling solution for educational institutions! 🎓  
Say goodbye to the manual, time-consuming process of creating timetables. This program automates teacher scheduling while considering real-world constraints like teacher availability, maximum workload, and non-consecutive teaching periods.

---

## 🌟 **Features**
- **Dynamic Scheduling**: Automatically generates timetables while handling constraints like teacher absences, non-consecutive periods, and subject limits.  
- **User-Friendly Output**: Produces a beautifully formatted, color-coded Excel timetable for seamless use.  
- **Constraint Optimization**: Ensures no teacher exceeds their maximum workload or teaches consecutive periods in the same class.  
- **Customizable**: Easily update teacher lists, subjects, and constraints by modifying input files.  
- **Fallback Mechanism**: Guarantees no empty periods, even under tight constraints.

---

## 🎯 **Why This Project?**
Creating school timetables is often a tedious, error-prone task. As someone passionate about solving real-world problems with technology, I wanted to develop a system that combines **automation**, **efficiency**, and **ease of use** to transform this process. This project reflects the power of Python and computational logic in simplifying complex logistical challenges.  

---

## 🚀 **How It Works**
1. **Input Teacher Data**:
   - The program reads teacher names and subjects from a file (`teachers.txt`).
   - Absent teachers can be dynamically excluded from the scheduling process.
2. **Assign Teachers**:
   - Teachers are assigned to periods based on constraints:
     - Non-consecutive teaching periods.
     - Maximum teaching load (default: 7 periods/day).
     - Balanced subject distribution across classes.
3. **Generate Timetable**:
   - The program creates a clear, color-coded Excel file (`timetable.xlsx`) with the generated schedule.
4. **Output**:
   - Each cell represents a teacher assigned to a specific period and class, with subject colors for better visualization.

---

## 📂 **Project Structure**
```plaintext
📁 Teacher-Timetable-Generator/
├── 📄 teachers.txt       # Input file with teacher names and subjects
├── 📄 main.py       # Main Python script
└── 📄 README.md          # This readme file
