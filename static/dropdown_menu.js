
$(document).ready(function() {
    var booksBybookCategory = {
        'School Textbooks': ['Class 1', 'Class 2', 'Class 3', 'Class 4', 'Class 5', 'Class 6', 'Class 7', 'Class 8', 'Class 9', 'Class 10', 'Class 11', 'Class 12','Other'],
        'Higher Education Textbooks': ['English Honours', 'Mathematics Honours', 'Physics Honours', 'Chemistry Honours', 'Economics Honours', 'History Honours', 'Political Science Honours', 'Computer Science Honours', 'Sociology Honours', 'Biotechnology Honours', 'Commerce Honours', 'Accountancy Honours','Other'],
        'Exam Preparation Books': ['SSC GD', 'NDA', 'Railway Exam', 'UPSC Civil Services', 'IBPS PO', 'CAT', 'JEE Main', 'NEET', 'GATE', 'CLAT', 'UGC NET', 'CTET','Other'],
        'Novel Books': ['Romantic', 'Comedy', 'Mystery', 'Science Fiction', 'Fantasy', 'Historical Fiction', 'Thriller', 'Horror', 'Drama', 'Adventure', 'Biography', 'Young Adult','Other']
    };
    
    var subjectsByClass = {
        'Class 1': ['English', 'Mathematics', 'Hindi', 'Environmental Studies','Other'],
        'Class 2': ['English', 'Mathematics', 'Hindi', 'Environmental Studies','Other'],
        'Class 3': ['English', 'Mathematics', 'Hindi', 'Environmental Studies','Other'],
        'Class 4': ['English', 'Mathematics', 'Hindi', 'Environmental Studies','Other'],
        'Class 5': ['English', 'Mathematics', 'Hindi', 'Environmental Studies','Other'],
        'Class 6': ['English', 'Mathematics', 'Science', 'Social Studies', 'Hindi','Other'],
        'Class 7': ['English', 'Mathematics', 'Science', 'Social Studies', 'Hindi','Other'],
        'Class 8': ['English', 'Mathematics', 'Science', 'Social Studies', 'Hindi','Other'],
        'Class 9': ['English', 'Mathematics', 'Science', 'Social Studies', 'Hindi','Other'],
        'Class 10': ['English', 'Mathematics', 'Science', 'Social Studies', 'Hindi','Other'],
        'Class 11': ['English', 'Mathematics', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'Economics', 'Accountancy', 'Business Studies','Other'],
        'Class 12': ['English', 'Mathematics', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'Economics', 'Accountancy', 'Business Studies','Other'],
    };

    var subjectsByHigherClass = {
        'English Honours': ['English Literature', 'Critical Thinking', 'Grammar and Composition', 'World Literature', 'Contemporary Literature', 'Other'],
        'Mathematics Honours': ['Calculus', 'Linear Algebra', 'Abstract Algebra', 'Number Theory', 'Probability and Statistics', 'Other'],
        'Physics Honours': ['Classical Mechanics', 'Electromagnetism', 'Quantum Mechanics', 'Thermodynamics', 'Astrophysics', 'Other'],
        'Chemistry Honours': ['Inorganic Chemistry', 'Organic Chemistry', 'Physical Chemistry', 'Analytical Chemistry', 'Biochemistry', 'Other'],
        'Economics Honours': ['Microeconomics', 'Macroeconomics', 'International Economics', 'Econometrics', 'Development Economics', 'Other'],
        'History Honours': ['Ancient History', 'Medieval History', 'Modern History', 'World History', 'Historiography', 'Other'],
        'Political Science Honours': ['Political Theory', 'Comparative Politics', 'International Relations', 'Public Administration', 'Political Philosophy', 'Other'],
        'Computer Science Honours': ['Data Structures', 'Algorithms', 'Database Management', 'Operating Systems', 'Computer Networks', 'Other'],
        'Sociology Honours': ['Introduction to Sociology', 'Social Theory', 'Research Methods', 'Cultural Sociology', 'Gender Studies', 'Other'],
        'Biotechnology Honours': ['Cell Biology', 'Genetics', 'Biochemistry', 'Molecular Biology', 'Bioprocess Engineering', 'Other'],
        'Commerce Honours': ['Financial Accounting', 'Cost Accounting', 'Business Law', 'Business Statistics', 'Marketing Management', 'Other'],
        'Accountancy Honours': ['Financial Accounting', 'Cost Accounting', 'Management Accounting', 'Taxation', 'Auditing', 'Other'],
        
    }

    function updateBookOptions() {
        var selectedCategory = $('#bookCategory').val();
        
        var books;
        $('#subCategory').empty();
        $('#subject').remove();
        
            books = booksBybookCategory[selectedCategory];
            $('#subCategory').append('<option value="" disabled selected> Select SubCategory</option>');
            for (var k = 0; k < books.length; k++) {
                $('#subCategory').append('<option value="' + books[k] + '">' + books[k] + '</option>');
            }
    }

    function updateSubjectOptions(){
        var selectedCategory = $('#bookCategory').val();
        var selectedClass = $('#subCategory').val();
        var sub;
        if(selectedCategory == 'School Textbooks'){
            sub = subjectsByClass[selectedClass];
        }else{
            sub = subjectsByHigherClass[selectedClass];
        }
        
        
        $('#subject').remove();
        $('#subject').empty();
        var $subjectDropdown = $('<select id="subject" name="subject"><option value="" disabled selected>Select Subject</option></select>');
            for (var j = 0; j < sub.length; j++) {
                $subjectDropdown.append('<option value="' + sub[j] + '">' + sub[j] + '</option>');
            }
            $('#sub-Category').append($subjectDropdown);

    }
    $('#subCategory').change(function() {
        updateSubjectOptions();
    });
    $('#bookCategory').change(function() {
        updateBookOptions();
    });
    // Initial update of book options
    updateBookOptions();
    
});
