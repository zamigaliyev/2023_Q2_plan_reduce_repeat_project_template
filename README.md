# 2023_Q2_plan_reduce_repeat_project_template

# As-Built Doc
## Release 2

### Stakeholders
- **Developers:**
  - Shahriyar Rzayev
  - Cavidan Hasanli
  - Namig Alasgarov
- **Ops:**
  - Ruslan Jababrov
- **SRE:**
  - Zamig Aliyev

### Code Changes
- **Security Fixes:**
  - Fixed the SQL injection vulnerability (Tk-205).
- **Feature Additions:**
  - Added a new catalog for exotic plants (Tk-203).
  - Re-arranged catalog menu in the UI (Tk-202).
  - Added order processor to decouple UI from order processing (Tk-201).

### Data and System Changes
- **Data Model Changes:**
  - Added new tables for the exotic plants catalog (Tk-203).
  - Modified existing tables to accommodate the new catalog structure.
  - Database schema was updated to support the decoupled order processor (Tk-201).

### Design Decision Highlights
- The introduction of a new catalog required additional memory resources. The decision to decouple the order processor from the UI was made to prevent the application from becoming CPU-bound during order processing.

### Test Section
- **Test Results:**
  - All test cases for the new catalog feature passed.
  - Load tests indicated a 25% increase in RAM usage without a significant impact on CPU usage.
  - Order processing tests showed that the new system can handle twice the previous load.

### Deployment Notes
- **Deployment Process:**
  - The deployment process remains manual but has been optimized to include additional resource allocation during the release window to prevent downtime.
- **Scripts:**
  - Additional scripts were executed to migrate the database and apply schema changes.
