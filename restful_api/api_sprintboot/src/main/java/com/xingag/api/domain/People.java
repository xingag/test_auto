package com.xingag.api.domain;


/***
 * 数据库映射对象（Mysql）
 */
public class People {
    private int id;
    private String name;
    private int age;
    private boolean extra;

    public People() {
    }

    public People(int id, String name, int age, boolean extra) {
        this.id = id;
        this.name = name;
        this.age = age;
        this.extra = extra;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public boolean isExtra() {
        return extra;
    }

    public void setExtra(boolean extra) {
        this.extra = extra;
    }
}
