International Software Testing Qualifications Board (ISTQB®)
This is the website which gives software testing certifications and this course is adapted from the foundation-level certificate course and is based on the curriculum specified for the foundation-level certificate Exam.

https://www.istqb.org/about-us.html

When detailing software testing cases, talk about the when, where, and how the test was performed.

## Software Testing

in 1947, the first bug was born, a moth that flew in and was zapped by
the Mark II computer at Harvard.

Cases

- Disney's Lion King (1994-1995): Disney build a CD-ROM Lion King game, which ended
  up causing conmotion due to Disney only testing their game in the computers of their
  own company. The game was not compatible with the computers of the rest of the world,
  and Disney had to recall all the games.

- Intel Pentium Floating-Poing Division bug (1994): Intel released the pentium CPU, which had a bug
  in the floating-point division. The team at Intel notices the bug, but decided there was no need to fix it because it only happened on extremely complex calculations.

In 2020, Citibank intended to send around $7.8 million in interest payments using a banking system called Oracle FLEXCUBE. However, due to employees "not filling enough fields in the form," approximately $900 million was mistakenly sent instead. This significant overpayment occurred despite transactions of this size requiring approval from three different people, all of whom reportedly thought the form was filled out correctly. As a result of this error, Citibank was unable to recover around $500 million of the transferred funds.

when: 2020
where: Citibank
how: Employees not filling enough fields in the form
what: $900 million was mistakenly sent instead of $7.8 million
should have been validated by 3 people, and all gave their yes.

Given the highlight that Dave knew about the possible two-digit date bug, he still made the decision
to implement a two-digit year date instead of thinking on how to represent years greater than 2000.
This is a clear example of what a team of QA engineers and testers can prevent, something this impactful
would have never happened under teh review of a team of testers. This bug was detrimental due to the
huge cost and effort required to fix the problem, and the fact that it was a bug that could have been
easily avoided with proper testing and validation.

### Effective debugging

- Make errors reproducible
- Locate the source of the bug
