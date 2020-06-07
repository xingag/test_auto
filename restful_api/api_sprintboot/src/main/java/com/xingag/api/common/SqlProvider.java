package com.xingag.api.common;

import com.xingag.api.domain.People;
import org.apache.ibatis.jdbc.SQL;


public class SqlProvider {

    /***
     * 使用MyBatis的SQL方法来更新sql语句
     *
     * @return
     */
    public String updatePeopleSql(People people) {

        //包含表名，要更新的字段，更新条件（id）
        //最后组装成新的SQL语句
        return new SQL() {{
            UPDATE("people");

            if (null != people.getName()) {
                SET("name=#{name}");
            }
            SET("age=#{age}");
            SET("extra=#{extra}");
            WHERE("id=#{id}");
        }}.toString();
    }
}
