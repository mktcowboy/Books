# Books

A working library of books, notes, summaries, lectures, speeches, and mind maps.

## What is here

- `summaries/` contains markdown notes organized by topic.
- `books/` contains source books and reference texts.
- `mindmaps/` contains visual summaries and study maps.
- `speaches/` contains speeches and related source material.
- `FILE_INDEX.md` is a generated index of the library content.

## Updating the indexes

Run the generator after adding, moving, or removing library files:

```bash
python3 auto_update_readme_tree.py
```

The script refreshes the README book tree and rewrites `FILE_INDEX.md`. Generated files and automation files are intentionally ignored by the tree.

## Book File Tree

<!-- file-tree:start -->
```text
Books/
├── books/
│   ├── A Practical Guide to Quant Vol Trading - Bloch 011516.pdf
│   ├── Alex_Reinhart-Statistics_Done_Wrong-EN.pdf
│   ├── Analysis of Financial Time Series.pdf
│   ├── convex_optimization.pdf
│   ├── Critique of Interventionism - Ludwig Mises.pdf
│   ├── Elements of Statistical Learning.pdf
│   ├── Empirical market structure.pdf
│   ├── Finding Alphas_ A Quant Approach to Building Trading Strategies - Tulchinsky.pdf
│   ├── Football Analytics with Python & R_ Learning Data Science Through the Lens of Sports.pdf
│   ├── Longstaff-schwartz algo for american option pricing.pdf
│   ├── Mises, Ludwig von - Human Action - A Treatise on Economics.pdf
│   ├── Monte Carlo methods in financial engineerin-Paul Glasserman-Springer (2004).pdf
│   ├── On the Genealogy of Morals - Nietzsche.pdf
│   ├── Stochastic Calculus for Finance I The Binomial Asset Pricing Model - Shreve.pdf
│   ├── Stochastic Calculus for Finance II- Continuous-Time Models -Shreve.pdf
│   ├── The Anti-Capitalistic Mentality - LVM.pdf
│   ├── Toby Crabel - Day Trading With Short Term Price Patterns.pdf
│   └── Trading w the Momo Transformer - An Intelligent Interpretable Architecture - Wood.pdf
└── speaches/
    └── clarence-thomas-law-review-articles/
        ├── A_Humble_Justice.pdf
        ├── At_the_Front_of_the_Train_Justice_Thomas_Reexamines_the_Administrative_State.pdf
        ├── But_For_the_Grace_Of_God_There_Go_I_Justice_Thomas_And_The_Little_Guy.pdf
        ├── Confronting_the_Administrative_State.pdf
        ├── Fisher_v._University_Of_Texas_and_the_Future_of_Affirmative_Action_in_Higher_Education.pdf
        ├── How_Justice_Thomas_Determines_the_Original_Meaning_of_Article_II_of_the_Constitution.pdf
        ├── Justice_Thomas_and_the_Originalist_Turn_in_Administrative_Law.pdf
        ├── Justice_Thomas_Criminal_Justice_and_Originalisms_Legitimacy.pdf
        ├── No_Entrenchment_Thomas_on_the_Hobbs_Act_the_Ocasio_Mess_and_the_Vagueness_Doctrine.pdf
        ├── The_Free_Speech_Jurisprudence_of_Clarence_Thomas.pdf
        ├── The_Jurisprudence_of_Clarence_Thomas.pdf
        ├── The_Truth_About_Clarence_Thomas_And_The_Need_For_New_Black_Leadership.pdf
        └── To_Help_Not_To_Hurt_Justice_Thomass_Equality_Canon.pdf
```
<!-- file-tree:end -->
