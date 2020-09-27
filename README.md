# tk-engine

**Description:**<br>
In short words, the purpose of this project is to **_represent testing knowledge as logic rules_** in a **BRMS**.

**Who will use it?**<br>
Anyone who want to automate the process of taking decisions on **what** to test.

**Scope:**<br>
* Web front-end testing.
* Mobile testing.

**Out of scope:**<br>
* Web back-end testing _(maybe in future)_.
* Desktop testing _(maybe in future)_.

**Requirements:**<br>
* This application should be deployable in any platform.
* This application should output a fact or a group of facts about testing.
* This application should cover general testing techniques.
* This application should cover general functional knowledge.
* This application should cover general non-functional knowledge.
* This application should **not** be tight to any specific domain knowledge.
    * Specific domain knowledge should be responsibility of the company/person using it, for example:
        * Financials knowledge.
        * Healthcare knowledge.
        * E-commerce knowledge.
        * etc...

**How it works:**<br>
Based on a group of facts, it will analyze with a set of already created rules and output one or a group of facts.<br>
 
**What if the results are not precise enough?**<br>
The facts can be confirmed by any specialist, in case it's not precise, the specialist can: <br>
1. Get the output from the previous attempt.
2. Edit the incorrect fact or add a missing fact.
3. Pass it as input again to the application.

**Frameworks/tools/stack that will be used on this project:**
  * Drools.
  * Java 11+.
  * Spring-boot
  * Maven.
  * JUnit 5.
  
**Observations:**<br>
  * This application is meant to be a http RPC API and not REST/RESTful API.
