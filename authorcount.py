import re
# Use the provided raw LaTeX text directly (trimmed version for memory efficiency)
raw_latex = r"""
\begin{cvpubs}

   \cvpub{J16 - \textbf{Borchers, C.}, Zhang, J., Fleischer, H., Schanze, S., Aleven, V. \& Baker, R. S. (accepted). Large Language Models Generalize SRL Prediction to New Languages Within But Not Between Domains. \textit{Journal of Educational Data Mining}.}{}{}
   
   \cvpub{J15 -- \textbf{Borchers, C.} \& Pardos, Z. A. (2025). Course Load Analytics Interventions on Higher Education Course Selection: Experimental Evidence. \textit{Journal of Learning Analytics}. \url{https://doi.org/10.18608/jla.2025.8473}}{}{}

   \cvpub{J14 -- \textbf{Borchers, C.}, Fleischer, H., Schanze, S., Scheiter, K., \& Aleven, V. (2025). High scaffolding of an unfamiliar strategy improves conceptual learning but reduces enjoyment compared to low scaffolding and strategy freedom. \textit{Computers \& Education}, 236, 105364. \url{https://doi.org/10.1016/j.compedu.2025.105364}}{}{}

   \cvpub{J13 -- \textbf{Borchers, C.}, Wang, Y., Hodge, E., \& Rosenberg, J. M. (2025). Decoding Sentiment Signals: Lessons from the Political Reception of the Common Core and Next Generation Science Standards. \textit{Educational Researcher}. \url{https://doi.org/10.3102/0013189X251336206}}{}{}

   \cvpub{J12 -- \textbf{Borchers, C.}, Xu, Y., \& Pardos, Z. A. (2025). Workload Overload? Late Enrollment Leads to Course Dropout. \textit{Journal of Educational Data Mining}. \url{https://doi.org/10.5281/zenodo.14907388}}{}{}

   \cvpub{J11 -- \textbf{Borchers, C.}, Darriet, C., Rosenberg, J., \& L\'opez, F. (2025). Dual Intent in Dual-language Programs: Internet Data Mining of School District Communications. \textit{TechTrends}. \url{https://doi.org/10.1007/s11528-025-01049-1}}{}{}

   \cvpub{J10 --\textbf{Borchers, C.}, Fleischer, H., Yaron, D. J., McLaren, B. M., Scheiter, K., Aleven, V., \& Schanze, S. (2025). Problem-Solving Strategies in Stoichiometry Across Two Intelligent Tutoring Systems: A Cross-National Study. Journal of Science Education and Technology.} \url{https://doi.org/10.1007/s10956-024-10197-7}{}{}
   
    \cvpub{J9 -- Zhang, L., Lin, J., Sabatini, J., \textbf{Borchers, C.}, Weitekamp, D., Cao, M., Hollander, J., Hu, X., \& Graesser, A. C. (2025). Data Augmentation for Sparse Multidimensional Learning Performance Data Using Generative AI. IEEE Transactions on Learning Technologies.} \url{https://doi.org/10.1109/TLT.2025.3526582}{}{}

   \cvpub{J8 -- Pritchard, C., \textbf{Borchers, C.}, Rosenberg, J. M., Fox, A. K., \& Stegenga, S. M. (2024). The datafication of student information on X (Twitter). \textit{Computers and Education Open, 7, 100197}. \url{https://doi.org/10.1016/j.caeo.2024.100197}}{}{}

    \cvpub{J7 -- \textbf{Borchers, C.}*, Rosenberg, J.*, \& Swartzentruber, R. M.* (2023). Facebook Post Data: A Primer for Educational Research. \textit{Educational Technology Research and Development.} \url{https://doi.org/10.1007/s11423-023-10269-2}}{}{}

    \cvpub{J6 -- \textbf{Borchers, C.}*, Eder, T. F.*, Richter, J., Keutel, C., Huettig, F., \& Scheiter, K. (2023). A Time Slice Analysis of Dentistry Students’ Visual Search Strategies and Pupil Dilation during Diagnosing Radiographs. \textit{PloS one}. \url{https://doi.org/10.1371/journal.pone.0283376}}{}{}

    \cvpub{J5 -- Pardos, Z. A., \textbf{Borchers, C.}, \& Yu, R. (2023). Credit hours is not enough: Explaining undergraduate perceptions of course workload using LMS records. \textit{The Internet and Higher Education, 56}, 100882. \url{https://doi.org/10.1016/j.iheduc.2022.100882}}{}{}
        
    \cvpub{J4 -- Rosenberg, J., \textbf{Borchers, C.}, Stegenga, S., Burchfield, M., Anderson, D., \& Fischer, C. (2022). How educational institutions reveal students' personally identifiable information on Facebook. \textit{Learning, Media and Technology}. Advanced Online Publication. \url{https://doi.org/10.1080/17439884.2022.2140672}}{}{}

    \cvpub{J3 -- Rosenberg, J., \textbf{Borchers, C.}, Burchfield, M., Anderson, D., Stegenga, S., \& Fischer, C. (2022). Posts About Students on Facebook: A Data Ethics Perspective. \textit{Educational Researcher}. Advanced Online Publication. \url{https://doi.org/10.3102/0013189X221120538}}{}{}

    \cvpub{J2 -- Rosenberg, J., Burchfield, M., \textbf{Borchers, C.}, Gibbons, B., Anderson, D., \& Fischer, C. (2021). Social media and students’ privacy: What schools and districts should know. \textit{Phi Delta Kappan, 103}(2), 49-53. \url{https://doi.org/10.1177/00317217211051145}}{}{}

    \cvpub{J1 -- Rosenberg, J., \textbf{Borchers, C.}, Dyer, E., Anderson, D. \& Fischer, C. (2021). Understanding Public Sentiment About Educational Reforms: The Next Generation Science Standards on Twitter. \textit{AERA Open, 7}(1), 1-17. \url{https://doi.org/10.1177/23328584211024261}}
\end{cvpubs}

%---------------------------------------------------------
\cvsubsection{Conference Proceedings [Peer-Reviewed]}
%---

\begin{cvpubs}

    \cvpub{C37 -- Fleischer, H., Noglik, A., \textbf{Borchers, C.}, \& Schanze, S. (in-press). Does Student Learning Rate Depend on Feedback Type and Prior Knowledge? \textit{Proceedings of the 18th International Conference on Educational Data Mining (EDM 2025)}. Palermo, Italy.}

    \cvpub{C36 -- Jin, Q., \textbf{Borchers, C.}, Fanscali, S., \& Aleven, V. (in-press). Predicting Teacher Interventions in K-12 Classrooms Using Disengagement, Struggle and Help-Seeking. \textit{Proceedings of the 18th International Conference on Educational Data Mining (EDM 2025)}. Palermo, Italy.}

    \cvpub{C35 -- Simon, S., Tajik, E., \textbf{Borchers, C.}, Shahrokhian, B., Sankaranarayanan, S., Balzan, F., Strauss, S., Viswanathan, S. A., Atas, A. H., Carapina, M., Liang, L., \& Celik, B. (in-press). Comparing Human and LLM-Generated Inductive Thematic Analyses: Assessing Agreement in Coding Consistency and Interpretative Accuracy. \textit{Proceedings of 26th International Conference on Artificial Intelligence in Education (AIED)}. Palermo, Italy.}

    \cvpub{C34 -- \textbf{Borchers, C.}, Houk, A., Aleven, V., \& Koedinger, K. R. (in-press). Engagement and Learning Benefits of Goal Setting with Rewards in Human-AI Tutoring. \textit{Proceedings of 26th International Conference on Artificial Intelligence in Education (AIED)}. Palermo, Italy.}

    \cvpub{C33 -- \textbf{Borchers, C.}, Nguyen, H. T., Carvalho, P. F., Koedinger, K. R., \& Aleven, V. (in-press). Involving Parents and Caregivers in Intelligent Tutoring Systems: A Design Probe Study. \textit{Proceedings of 26th International Conference on Artificial Intelligence in Education (AIED)}. Palermo, Italy.}

    \cvpub{C32 -- \textbf{Borchers, C.} \& \textit{Shou, T.} (in-press). Can Large Language Models Match Tutoring System Adaptivity? A Benchmarking Study. \textit{Proceedings of 26th International Conference on Artificial Intelligence in Education (AIED)}. Palermo, Italy.}

    \cvpub{C31 -- \textbf{Borchers, C.}, Peng, C., Lyu, Q., Carvalho, P. F., Koedinger, K. R., \& Aleven, V. (in-press). Student Perceptions of Adaptive Goal Setting Recommendations: A Design Prototyping Study. \textit{Proceedings of 26th International Conference on Artificial Intelligence in Education (AIED)}. Palermo, Italy.}

    \cvpub{C30 -- Thomas, D. R., \textbf{Borchers, C.}, Bhushan, S., Kakarla, S., Houk, A., Abboud, R., Gatz, E., Gupta, S., \& Koedinger, K. R. (in-press). Improving Open-Response Assessment with LearnLM. \textit{Proceedings of 26th International Conference on Artificial Intelligence in Education (AIED)}. Palermo, Italy.}

    \cvpub{C29 -- Gurung, A., Lin, J., Huang, Z., \textbf{Borchers, C.}, Baker, R. S., Aleven, V., \& Koedinger, K. R. (in-press). Starting Seatwork Earlier as a Valid Measure of Student Engagement. \textit{Proceedings of the 18th International Conference on Educational Data Mining (EDM)}. Palermo, Italy.}

    \cvpub{C28 -- \textbf{Borchers, C.} (in-press). Toward Sufficient Statistical Power in Algorithmic Bias Assessment: A Test for ABROCA. \textit{Proceedings of the 18th International Conference on Educational Data Mining (EDM)}. Palermo, Italy.}

    \cvpub{C27 -- Thomas, D. R., \textbf{Borchers, C.}, Kakarla, S., Lin, J., Bhushan, S., Guo, B., Gatz, E., \& Koedinger, K. R. (2025). Do Tutors Learn from Equity Training and Can Generative AI Assess It? \textit{Proceedings of the 15th International Learning Analytics and Knowledge Conference (LAK)}. Dublin, Ireland. ACM. \url{https://doi.org/10.1145/3706468.3706531}}

    \cvpub{C26 -- Thomas, D. R., \textbf{Borchers, C.}, Kakarla, S., Lin, J., Bhushan, S., Guo, B., Gatz, E., \& Koedinger, K. R. (2025). Does Multiple Choice Have a Future in the Age of Generative AI? A Posttest-Only RCT. \textit{Proceedings of the 15th International Learning Analytics and Knowledge Conference (LAK)}. Dublin, Ireland. ACM. \url{https://doi.org/10.1145/3706468.3706530}}

    \cvpub{C25 -- \textit{Venugopalan, D.}, \textit{Yan, Z.}, \textbf{Borchers, C.}, Lin, J., \& Aleven, V. (2025). Combining Large Language Models with Tutoring System Intelligence: A Case Study in Caregiver Homework Support. \textit{Proceedings of the 15th International Learning Analytics and Knowledge Conference (LAK)}. Dublin, Ireland. ACM. \url{https://doi.org/10.1145/3706468.3706516}}

    \cvpub{C24 -- Butler, R., \textbf{Borchers, C.}, Asher, M., Lee, Y., Karnataki, S., Dangi, S., Athreya, S., Stamper, J., Ogan, A., \& Carvalho, P. (2025). Does the Doer Effect Generalize to Non-WEIRD Populations? Toward Analytics in Radio and Phone-Based Learning. \textit{Proceedings of the 15th International Learning Analytics and Knowledge Conference (LAK)}. Dublin, Ireland. ACM. \url{https://doi.org/10.1145/3706468.3706505}}

    \cvpub{C23 -- \textbf{Borchers, C.} \& Baker, R. S. (2025). ABROCA Distributions for Algorithmic Bias Assessment: Considerations Around Interpretation. \textit{Proceedings of the 15th International Learning Analytics and Knowledge Conference (LAK)}. Dublin, Ireland. ACM. \url{https://doi.org/10.1145/3706468.3706498}}

    \cvpub{C22 -- \v{S}v\'{a}bensk\'{y}, V., \textbf{Borchers, C.}, Cloude, E. B., \& Shimada, A. (2025). Evaluating the Impact of Data Augmentation on Predictive Model Performance. \textit{Proceedings of the 15th International Learning Analytics and Knowledge Conference (LAK)}. Dublin, Ireland. ACM. \url{https://doi.org/10.1145/3706468.3706485}}	

    \cvpub{C21 -- \textbf{Borchers, C.}*, Ooge, J.*, \textit{Peng, C.}, \& Aleven, V. (2025). How Learner Control and Explainable Learning Analytics About Skill Mastery Shape Student Desires to Finish and Avoid Loss in Tutored Practice. \textit{Proceedings of the 15th International Learning Analytics and Knowledge Conference (LAK)}. Dublin, Ireland. ACM. \url{https://doi.org/10.1145/3706468.3706484}}

    \cvpub{C20 -- Zhang, J.*, \textbf{Borchers, C.}*, \& Barany, A. (2024). Studying the Interplay of Self-Regulated Learning Cycles and Scaffolding Through Ordered Network Analysis Across Three Tutoring Systems. \textit{Proceedings of the International Conference on Quantitative Ethnography (ICQE)}, Philadelphia, PA, USA. \url{https://doi.org/10.1007/978-3-031-76335-9_17}}

    \cvpub{C19 -- Yang, K. B.*, \textbf{Borchers, C.}*, Falhs, A.-C., Echeverria, V., Karumbaiah, S., Rummel, N., \& Aleven, V. (2024). Leveraging Multimodal Classroom Data for Teacher Reflection: Teachers' Preferences, Practices, and Privacy Considerations. \textit{Proceedings of the 19th European Conference on Technology Enhanced Learning (EC-TEL)}, Krems, Austria. \url{https://doi.org/10.1007/978-3-031-72315-5_34}}

    \cvpub{C18 -- Baucks, F.*, Schmucker, R.*, \textbf{Borchers, C.}, Pardos, Z. A., \& Wiskott, L. (2024). Gaining Insights into Group-Level Course Difficulty via Differential Course Functioning. \textit{Proceedings of the Tenth (2024) ACM Conference on Learning@Scale (L@S)}. Atlanta, GA, USA. \url{https://doi.org/10.1145/3657604.3662028}}

    \cvpub{C17 -- \textbf{Borchers, C.}, Xu, Y., \& Pardos, Z. A. (2024). Are You an Early Dropper or Late Shopper? Mining Enrollment Transaction Data to Study Procrastination in Higher Education. \textit{Proceedings of the 17th International Conference on Educational Data Mining (EDM)}. Atlanta, GA, USA. \url{https://doi.org/10.5281/zenodo.12729852}}

    \cvpub{C16 -- Zhang, J., \textbf{Borchers, C.}, Aleven, V., \& Baker, R. S. (2024). Using Large Language Models to Detect Self-Regulated Learning in Think-Aloud Protocols. \textit{Proceedings of the 17th International Conference on Educational Data Mining (EDM)}. Atlanta, GA, USA. \url{https://doi.org/10.5281/zenodo.12729790}}
    
    \cvpub{C15 -- \textbf{Borchers, C.}, Yang, K., Lin, J., Rummel, N., Koedinger, K. R., \& Aleven, V. (2024). Combining Dialog Acts and Skill Modeling: What Chat Interactions Enhance Learning Rates During AI-Supported Peer Tutoring? \textit{Proceedings of the 17th International Conference on Educational Data Mining (EDM)}. Atlanta, GA, USA. \url{https://doi.org/10.5281/zenodo.12729784}}

    \cvpub{C14 -- \textbf{Borchers, C.}, Liu, X., Lee, H. H., \& Zhang, J. (2024). Ethical AIED and AIED Ethics: Toward Synergy Between AIED Research and Ethical Frameworks. \textit{Proceedings of 25th International Conference on Artificial Intelligence in Education (AIED) — BlueSky Track}. Recife, Brazil. \url{https://doi.org/10.1007/978-3-031-64315-6_2}}

    \cvpub{C13 -- Zhang, L., Lin, J., \textbf{Borchers, C.}, Sabatini, J., Hollander, J., Cao, M., \& Hu, X. (2024). Predicting Learning Performance with Large Language Models: A Study in Adult Literacy. \textit{Proceedings of the 26th International Conference On Human-Computer Interaction (HCII)}. Washington, DC, USA. \url{https://doi.org/10.1007/978-3-031-60609-0_24}}

    \cvpub{C12 -- \textit{Peng, C.}, \textbf{Borchers, C.}, \& Aleven, V. (2024). Designing Homework Support Tools for Middle School Mathematics Using Intelligent Tutoring Systems. \textit{Proceedings of the 2024 Annual Meeting of the International Society of the Learning Sciences (ISLS)}. Buffalo, NY, USA. \url{https://doi.org/10.22318/icls2024.989202}}

    \cvpub{C11 -- \textit{Nguyen, H. T.}, \textbf{Borchers, C.}, Xia, M., \& Aleven, V. (2024). Designing Tools for Caregiver Involvement in Intelligent Tutoring Systems for Middle School Mathematics. \textit{Proceedings of the 2024 Annual Meeting of the International Society of the Learning Sciences (ISLS)}. Buffalo, NY, USA. \url{https://doi.org/10.22318/icls2024.630637}}
    
    \cvpub{C10 -- \textbf{Borchers, C.}, Wang, Y., Karumbaiah, S., Ashiq, M., Shaffer, D. W., \& Aleven, V. (2024). Revealing Networks: Understanding Effective Teacher Practices in AI-Supported Classrooms using Transmodal Ordered Network Analysis. \textit{Proceedings of the 14th International Learning Analytics and Knowledge Conference (LAK)}. Kyoto, Japan. ACM. \url{https://doi.org/10.1145/3636555.3636892}}

    \cvpub{C9 -- \textbf{Borchers, C.}, Zhang, J., Baker, R. S., \& Aleven, V. (2024). Using Think-Aloud Data to Understand Relations between Self-Regulation Cycle Characteristics and Student Performance in Intelligent Tutoring Systems. \textit{Proceedings of the 14th International Learning Analytics and Knowledge Conference (LAK)}. Kyoto, Japan. ACM. \url{https://doi.org/10.1145/3636555.3636911}}

    \cvpub{C8 -- \textbf{Borchers, C.}, Carvalho, P. F., Xia, M., Liu, P., Koedinger, K. R., \& Aleven, V. (2023). What Makes Problem-Solving Practice Effective? Comparing Paper and AI Tutoring. \textit{Proceedings of the 18th European Conference on Technology Enhanced Learning (EC-TEL)}. Aveiro, Portugal. \url{https://doi.org/10.1007/978-3-031-42682-7_4}}

    \cvpub{C7 -- Karumbaiah, S., \textbf{Borchers, C.}, Shou, T., Falhs, A.-C., Liu, C., Nagashima, T., Rummel, N., \& Aleven, V. (2023). A Spatiotemporal Analysis of Teacher Practices in Supporting Student Learning and Engagement in an AI-enabled Classroom. \textit{Proceedings of the 24th International Conference on Artificial Intelligence in Education (AIED)}. Tokyo, Japan. \url{https://doi.org/10.1007/978-3-031-36272-9_37}}

    \cvpub{C6 -- \textit{Shou, T.}, \textbf{Borchers, C.}, Karumbaiah, S., \& Aleven, V. (2023). Optimizing Parameters for Accurate Position Data Mining in Diverse Classrooms Layouts. \textit{Proceedings of the 16th International Conference on Educational Data Mining (EDM)}. Bengaluru, India. \url{https://doi.org/10.5281/zenodo.8115685}}
    
    \cvpub{C5 -- \textbf{Borchers, C.}, Klein, L., Johnson, H., \& Fischer, C. (2023). Timing Matters: Inferring Educational Twitter Community Switching from Membership Characteristics. \textit{Proceedings of the 16th International Conference on Educational Data Mining (EDM)}. Bengaluru, India. \url{https://doi.org/10.5281/zenodo.8115752}}

    \cvpub{C4 -- Karumbaiah, S.*, \textbf{Borchers, C.}*, Falhs, A.-C.*, Holstein, K., Rummel, N., \& Aleven, V. (2023). Teacher Noticing and Student Learning in  Human-AI Partnered Classrooms: A Multimodal Analysis. \textit{Proceedings of the 2023 Annual Meeting of the International Society of the Learning Sciences (ISLS)}. Montr\'eal, Canada. \url{https://doi.org/10.22318/icls2023.151200}}

    \cvpub{C3 -- \textbf{Borchers, C.} \& Pardos, Z. A. (2023). Insights into undergraduate pathways using course load analytics. \textit{Proceedings of the 13th International Learning Analytics and Knowledge Conference (LAK)}. Arlington, TX, USA. ACM. \url{https://doi.org/10.1145/3576050.3576081}}

    \cvpub{C2 -- \textbf{Borchers, C.}, Rosenberg, J., Gibbons, B., Burchfield, M., \& Fischer, C. (2021). To Scale or Not to Scale: Comparing Popular Sentiment Analysis Dictionaries on Educational Twitter Data. \textit{Proceedings of the 14th International Conference on Educational Data Mining (EDM)}. Paris, France.}
    
    \cvpub{C1 -- Burchfield, M., Rosenberg, J., \textbf{Borchers, C.}, Thomas, T., Gibbons, B., \& Fischer, C. (2021). Are Violations of Student Privacy ``Quick and Easy''? Investigating the Privacy of Students’ Images and Names in the Context of K-12 Educational Institution’s Posts on Facebook. \textit{Proceedings of the 14th International Conference on Educational Data Mining (EDM)}. Paris, France.}
\end{cvpubs}

%---------------------------------------------------------
\cvsubsection{Workshop Publications [Peer-Reviewed]}
%---

\begin{cvpubs}

    \cvpub{W7 -- Sankaranarayanan, S., \textbf{Borchers, C.}, Simon, S., Tajik, E., Atas, A. H., Celik, B., Balzan, F., \& Shahrokhian, B. (2025). Automating Thematic Analysis with Multi-Agent LLM Systems. \textit{From Data to Discovery: LLMs for Qualitative Analysis in Education at LAK25}.}

    \cvpub{W6 -- \textbf{Borchers, C.}, Thomas, D. R., Lin, J., Abboud, R., \& Koedinger, K. R. (2025). Augmenting Human-Annotated Training Data with Large Language Model Generation and Distillation in Open-Response Assessment. \textit{Proceedings of the Second Workshop on Generative AI for Learning Analytics (GenAI-LA) at LAK25}.}

    \cvpub{W5 -- \textit{Kakarla, S.}, \textbf{Borchers, C.}, Thomas, D. R., Bhushan, S., \& Koedinger, K. R. (2025). Comparing Few-Shot Prompting of GPT-4 LLMs with BERT Classifiers for Open-Response Assessment in Tutor Equity Training. \textit{Proceedings of the Innovation and Responsibility in AI-Supported Education (iRAISE) Workshop at AAAI25}.}

    \cvpub{W4 -- Aleven, V., \textbf{Borchers, C.}, Huang, Y., Nagashima, T., McLaren, B., Carvalho, P., Popescu, O., Sewall, J., \& Koedinger, K. (2024). An Integrated Platform for Studying Learning with Intelligent Tutoring Systems: CTAT+TutorShop. \textit{Proceedings of the Fifth Annual Workshop on Learning@Scale 2024: A/B Testing and Platform-Enabled Learning Research}.}

     \cvpub{W3 -- Zhang, L., Lin, J., \textbf{Borchers, C.}, Cao, M., \& Hu, X. (2024). 3DG: A Framework for Using Generative AI for Handling Sparse Learner Performance Data From Intelligent Tutoring Systems. \textit{Proceedings of the First Workshop on Generative AI for Learning Analytics (GenAI-LA) at LAK24}.}

    \cvpub{W2 -- Han, Z. F., Lin, J., Gurung, A., Thomas, D. R., Chen, E., \textbf{Borchers, C.}, Gupta, S., \& Koedinger, K. R. (2024). Improving Assessment of Tutoring Practices using Retrieval-Augmented Generation. \textit{Proceedings of the AAAI2024 Workshop on AI for Education - Bridging Innovation and Responsibility}.}

    \cvpub{W1 -- \textbf{Borchers, C.}*, Gala, D. S.*, Gilburt, B.*, Oravkin, E., Bounsi, W., Asano, Y. M., \& Kirk, H. R. (2022). Looking for a Handsome Carpenter! Debiasing GPT-3 Job Advertisements. \textit{Proceedings of the 4th Workshop on Gender Bias in Natural Language Processing (NAACL)}.}
\end{cvpubs}

\cvsubsection{Conference Demo Publications [Peer-Reviewed]}

\begin{cvpubs}
\cvpub{D2 -- Yang, K., Zhao, Y., \textbf{Borchers, C.}, Fang, Y., Kim, J., Butt, A., Popescu, O., Gupte, S., Chiu, A., Shen, P., Rummel, N., \& Aleven, V. (2025). Reflecto: A Teacher Reflection Tool Leveraging Multimodal Learning and Teaching Analytics. \textit{26th International Conference on Artificial Intelligence in Education (AIED)}.}

    \cvpub{D1 -- Rao, J., \textbf{Borchers, C.}, \& Lin, J. (2024). Coursera-REC: Explainable MOOCs Course Recommendation using RAG-facilitated LLMs. \textit{25th International Conference on Artificial Intelligence in Education (AIED)}.}
\end{cvpubs}

""" 

# Step 1: Extract only content up to (year), (accepted), (in press), or (in-press)
entries = re.findall(r'\\cvpub\{(.*?)(?:\((?:\d{4}|accepted|in[- ]press))', raw_latex, re.IGNORECASE)

# Step 2: Remove LaTeX formatting and your own name
cleaned_entries = [re.sub(r'\\textbf\{Borchers, C\.\}|\\textit\{.*?\}', '', entry) for entry in entries]

# Step 3: Extract names using two common patterns
pattern1 = re.findall(r'([A-Z][a-z]+),\s([A-Z](?:\.\s?[A-Z]\.)?)', ' '.join(cleaned_entries))
pattern2 = re.findall(r'([A-Z](?:\.\s?[A-Z]\.?)?)\s([A-Z][a-z]+)', ' '.join(cleaned_entries))

# Step 4: Combine and clean
coauthors = {(fn.strip(), ln.strip()) for ln, fn in pattern1} | {(fn.strip(), ln.strip()) for fn, ln in pattern2}
coauthors = {name for name in coauthors if name[1] != "Borchers"}

# Step 5: Sort and print
sorted_coauthors = sorted(coauthors, key=lambda x: (x[1], x[0]))
print(f"Total unique co-authors: {len(sorted_coauthors)}")
for fn, ln in sorted_coauthors:
    print(f"{fn} {ln}")

