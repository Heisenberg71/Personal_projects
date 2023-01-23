[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=7845824&assignment_repo_type=AssignmentRepo)
# Resume Analyser
<!-- Replace the "RENAME_ME_WITH_YOUR_PROJECT_TITLE" in the text above with your project Title -->
Course: **CSE 702 - Artificial Intelligence Lab**            
Offered for: Session *2017-18*, Dept. of CSE, SEC
### Group \# **03**
<!-- Replace the "00" in the text above with your project group number. It should be anything between 01 to 25 -->
Group Name: **BugFinder**

## Contributors' Info
<!-- Fill the blanks with your information. change the last two letter of the registration numbers with the respective digits. Correct the "Session" if needed. -->
|                 |  Member 1           |  Member 2                     |
| --------------: | :--------:          | :--------:                    |
|            Name |  Samin Yasir                   |         Al-Mamun Salauddin                      |
| Registration \# | 2017331505          | 2017331534                    | 
|         Session |  2017-18            |  2017-18                      |
| GitHub Username |Heisenberg71         | Mamun-71                      |
|            Cell |01793592090          | 01609353793                   |
|           Email |samin99099@gmail.com | almamunsalaudding@gmail.com   |


Supervisor
-----------
**Enamul Hassan**         
Assistant Professor     
Department of Computer Science and Engineering          
Shahjalal University of Science and Technology       
[Faculty Profile](https://www.sust.edu/d/cse/faculty-profile-detail/590) and [GitHub Profile](https://github.com/enamcse)


## Project Idea
Our project collect job requirment and candidate resume as input and output the match percentage.
### Motivation
We understood basic concepts of AI,ML,NLP throughout this project.
<!-- Describe here why this project is being done. -->
### Scope
Filtering out the resume easily in any of organization.
<!-- Describe the domain space of the project. -->
### Platform
Web application
<!-- What is the environment requirement of the project? What is the OS? Is it for mobile, web, or general API? -->
### Project Brief
1. Our project takes job requirment PDF and resume PDF as input. It shows the match percentage of skills as output.
2. We used python package **pdfminer** to extract out the texts from job requirment PDF and resume PDF.
3. After getting the texts from the PDF's, python package **nltk** is used to extract out the skills from the candidate resume.
4. After getting the skills, cosine similarity between the skills and job requirment is calculated which will tell the match percentage.
<!-- Describe the project in brief. -->

## Project Deliverables
<!-- This table should reflect what are you going to submit. How your progresses would be visible. Note that, you have to create a corresponding issue in the GitHub issue to submit the work of any milestone. -->
<table>
<thead>
    <tr>
        <th>SL</th>
        <th>Milestone</th>
        <th>Details</th>
        <th>Comments</th>
        <th>Expected Submission Date</th>
        <th>Submission Date</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td> 1 </td>
        <td>40% Completion</td>
        <td>
        <ul>
            <!-- Change the following list with your project's checklist for 40% Completion. The following texts have no significance and it is put here just for beautifying. -->
            <li>User Interface : Streamlit :- an open-source app framework for Machine Learning</li>
            <li>Trying differnt types of model to get better pdf text extraction</li>
        </ul>
        </td>
        <!-- Initially make the following text empty. You have to fill it in the time of submission. -->
        <td>Some Machine Learning Models not work properly with the APIs</td>
        <!-- The following is the estimated submission date for this milestone. Change it as your need. -->
        <td>May 10, 2022</td>
        <!-- Initially make the following text empty. You have to fill it in the time of submission. -->
        <td>May 20, 2022</td>
    </tr>
    <tr>
        <td> 2 </td>
        <td>70% Completion</td>
        <td>
        <ul>
            <!-- Change the following list with your project's checklist for 70% Completion. The following texts have no significance and it is put here just for beautifying. -->
            <li>Deep Learning Model Adapting APIs:  pdfminer</li>
            <li>Deep Learning Model Adapting APIs:  nltk :: Natural Language Toolkit</li>
        </ul>
        </td>
        <!-- Initially make the following text empty. You have to fill it in the time of submission. -->
        <td>5 days early submission. Some API made the task easier. </td>
        <!-- The following is the estimated submission date for this milestone. Change it as your need. -->
        <td>May 20, 2022</td>
        <!-- Initially make the following text empty. You have to fill it in the time of submission. -->
        <td>June 3, 2022</td>
    </tr>
    <tr>
        <td> 3 </td>
        <td>100% Completion</td>
        <td>
        <ul>
            <!-- Change the following list with your project's checklist for 100% Completion. The following texts have no significance and it is put here just for beautifying. -->
            <li>Collecting Candidate resume</li>
            <li>Collecting Job requirment pdf from bdjobs.com</li>
            <li>Testing</li>
            <li>Project is Colmplete</li>
        </ul>
        </td>
        <!-- Initially make the following text empty. You have to fill it in the time of submission. -->
        <td>Delayed Submission without any genuine reason. Hence, penalty is must. </td>
        <!-- The following is the estimated submission date for this milestone. Change it as your need. -->
        <td>May 30, 2022</td>
        <!-- Initially make the following text empty. You have to fill it in the time of submission. -->
        <td>July 30, 2022</td>
    </tr>
</tbody>
</table>

## Project Presentation Slide
<!-- Upload the project presentation slide in GitHub in pdf format and drop a link here. The current link is a dummy one. -->
[Here](https://github.com/cse-702-2017/project-g03-bugfinder/blob/main/Resume%20Analyser.pdf) is the presentation slide of the project.

Technical Documentation/ Instruction to Deploy the Project
----------------------------------------------------------
<!-- Write a detailed documentation for a technical user who want to DEPLOY your project. It should be as detailed as possible. You can add a FAQ section if needed where basic troubleshooting questions should be answered. Adding Screenshot is appreciated. -->
1. Download and Install Streamlit from [this](https://streamlit.io) website.
2. Go to the comand promote and enter this command: **pip install pdfminer** to install pdfminer package.
3. To install nltk pakage write this command **pip install nltk**
4. To install this command **pip install pathlib** 

Non-Technical Documentation/ User-guide for the End-Users of the Project
------------------------------------------------------------------------
<!-- Write a detailed documentation for a non-technical user who want to USE THE FEATURES of your project. It should be as detailed as possible with proper screenshots. You may add a FAQ section if needed where common questions should be answered. Adding Screenshot is MUST. -->
1.Clone my project repository.

2.Go to the project folder where requirments.txt file is located and enter comand **pip install -r requirments.txt**.

3.Go to `192.168.0.1:8501` in your browser and observe a page like the following screenshot. 
![image](https://github.com/cse-702-2017/project-g03-bugfinder/blob/main/Project%20SS.png)If it is not found, contact the administrator.

4.Upload the resume and requirments pdf.

5.Observe the output.

Acknowledgement
--------
<!-- You should acknowledge every external help here. A table could be a good option. From Stackoverflow question to any conference/journal paper everything should be mentioned including its use in your project. You should include the contribution of your friend if you take it from anyone. -->
1.Stackoverflow

2.Google

3.Youtube

4.Official documentation of the packages used in the project.

Disclaimer and Non-Disclosure Agreement (NDA)
---------------------------------------------
<!-- In the following TWO pairs of square brackets, put an 'x' without quotes after reading and accepting the statements. -->
- [X] This is to certify that this project is done by the *Contributors* mentioned above and nothing is hidden from the supervisor. The external resource(s) used here is/are properly acknowledged above. If any proof of falsifying is found, then the supervisor and the corresponding authority would take the necessary actions.
- [X] This is to certify that the above mentioned *Contributors* are fully responsible for the confidentiality of the project. Any part of the project would NOT be shared publicly or privately without the prior permission of the supervisor mentioned above even after the publication of the result. If anything else happens, then the supervisor and the corresponding authority would take the necessary actions.

<!-- Thank you so much. -->
