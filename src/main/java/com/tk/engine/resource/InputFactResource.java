package com.tk.engine.resource;

import com.tk.engine.model.Input;
import org.kie.api.runtime.KieSession;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class InputFactResource {

    private final KieSession kieSession;

    public InputFactResource(KieSession kieSession) {
        this.kieSession = kieSession;
    }

    @PostMapping("/input")
    public Input inputFact(@RequestBody Input inputFact) {
        kieSession.insert(inputFact);
        kieSession.fireAllRules();
        return inputFact;
    }
}
