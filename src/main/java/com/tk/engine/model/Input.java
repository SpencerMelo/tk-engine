package com.tk.engine.model;

import java.util.List;

public class Input {
    private String type;
    private List<String> restrictions;
    private int min;
    private int max;

    public Input(String type, List<String> restrictions, int min, int max) {
        this.type = type;
        this.restrictions = restrictions;
        this.min = min;
        this.max = max;
    }

    public String getType() {
        return this.type;
    }

    public List<String> getRestrictions() {
        return this.restrictions;
    }

    public int getMin() {
        return min;
    }

    public int getMax() {
        return max;
    }

    public void setType(String type) {
        this.type = type;
    }

    public void setRestrictions(List<String> restrictions) {
        this.restrictions = restrictions;
    }

    public void setMin(int min) {
        this.min = min;
    }

    public void setMax(int max) {
        this.max = max;
    }
}
